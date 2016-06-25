import time
import six
import random

from urchin import reflection
from monotonic import monotonic as now

DEFAULT_INTERVAL = 60.0


def _nearest_boundary(last_run, spacing):
    """Find the nearest boundary in the past.

    The boundary is a multiple of the spacing with the last run as an offset.

    Eg if last run was 10 and spacing was 7, the new last run could be: 17, 24,
    31, 38...

    0% to 5% of the spacing value will be added to this value to ensure tasks
    do not synchronize. This jitter is rounded to the nearest second, this
    means that spacings smaller than 20 seconds will not have jitter.
    """
    current_time = now()
    if last_run is None:
        return current_time
    delta = current_time - last_run
    offset = delta % spacing
    # Add up to 5% jitter
    jitter = int(spacing * (random.random() / 20))
    return current_time - offset + jitter


class _PeriodicTasksMeta(type):
    def _add_periodic_task(cls, task):
        """Add a periodic task to the list of periodic tasks.

        The task should already be decorated by @periodic_task.

        :return: whether task was actually enabled
        """
        name = task._periodic_name

        if task._periodic_spacing < 0:
            #LOG.info(_LI('Skipping periodic task %(task)s because '
            #             'its interval is negative'),
            #         {'task': name})
            return False
        if not task._periodic_enabled:
            #LOG.info(_LI('Skipping periodic task %(task)s because '
            #             'it is disabled'),
            #         {'task': name})
            return False

        # A periodic spacing of zero indicates that this task should
        # be run on the default interval to avoid running too
        # frequently.
        if task._periodic_spacing == 0:
            task._periodic_spacing = DEFAULT_INTERVAL

        cls._periodic_tasks.append((name, task))
        cls._periodic_spacing[name] = task._periodic_spacing
        return True

    def __init__(cls, names, bases, dict_):
        """Metaclass that allows us to collect decorated periodic tasks."""
        super(_PeriodicTasksMeta, cls).__init__(names, bases, dict_)

        # NOTE(sirp): if the attribute is not present then we must be the base
        # class, so, go ahead an initialize it. If the attribute is present,
        # then we're a subclass so make a copy of it so we don't step on our
        # parent's toes.
        try:
            cls._periodic_tasks = cls._periodic_tasks[:]
        except AttributeError:
            cls._periodic_tasks = []

        try:
            cls._periodic_spacing = cls._periodic_spacing.copy()
        except AttributeError:
            cls._periodic_spacing = {}

        for value in cls.__dict__.values():
            if getattr(value, '_periodic_task', False):
                cls._add_periodic_task(value)


@six.add_metaclass(_PeriodicTasksMeta)
class PeriodicTasks(object):
    def __init__(self):
        super(PeriodicTasks, self).__init__()
        #self.conf = conf
        #self.conf.register_opts(_options.periodic_opts)
        self._periodic_last_run = {}
        for name, task in self._periodic_tasks:
            self._periodic_last_run[name] = task._periodic_last_run

    def add_periodic_task(self, task):
        """Add a periodic task to the list of periodic tasks.

        The task should already be decorated by @periodic_task.
        """
        if self.__class__._add_periodic_task(task):
            self._periodic_last_run[task._periodic_name] = (
                task._periodic_last_run)

    def run_periodic_tasks(self, context, raise_on_error=False):
        """Tasks to be run at a periodic interval."""
        idle_for = DEFAULT_INTERVAL
        for task_name, task in self._periodic_tasks:
            if (task._periodic_external_ok and not
               self.conf.run_external_periodic_tasks):
                continue
            cls_name = reflection.get_class_name(self, fully_qualified=False)
            full_task_name = '.'.join([cls_name, task_name])

            spacing = self._periodic_spacing[task_name]
            last_run = self._periodic_last_run[task_name]

            # Check if due, if not skip
            idle_for = min(idle_for, spacing)
            if last_run is not None:
                delta = last_run + spacing - now()
                if delta > 0:
                    idle_for = min(idle_for, delta)
                    continue

            # LOG.debug("Running periodic task %(full_task_name)s",
            #           {"full_task_name": full_task_name})
            self._periodic_last_run[task_name] = _nearest_boundary(
                last_run, spacing)

            try:
                task(self, context)
            except Exception:
                if raise_on_error:
                    raise
                # LOG.exception(_LE("Error during %(full_task_name)s"),
                #               {"full_task_name": full_task_name})
            time.sleep(0)

        return idle_for

