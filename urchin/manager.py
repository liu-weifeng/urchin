from urchin import periodic_task


class PeriodicTasks(periodic_task.PeriodicTasks):
    def __init__(self):
        super(PeriodicTasks, self).__init__()


class Manager(PeriodicTasks):
    def __init__(self, host=None, db_driver=None, service_name='undefined'):
        # if not host:
        #     host = CONF.host
        # self.host = host
        # self.backdoor_port = None
        # self.service_name = service_name
        # self.notifier = rpc.get_notifier(self.service_name, self.host)
        # self.additional_endpoints = []
        # super(Manager, self).__init__(db_driver)
        pass

    def periodic_tasks(self, context, raise_on_error=False):
        """Tasks to be run at a periodic interval."""
        return self.run_periodic_tasks(context, raise_on_error=raise_on_error)

    def init_host(self):
        """Hook to do additional manager initialization when one requests
        the service be started.  This is called before any service record
        is created.

        Child classes should override this method.
        """
        pass

    def cleanup_host(self):
        """Hook to do cleanup work when the service shuts down.

        Child classes should override this method.
        """
        pass

    def pre_start_hook(self):
        """Hook to provide the manager the ability to do additional
        start-up work before any RPC queues/consumers are created. This is
        called after other initialization has succeeded and a service
        record is created.

        Child classes should override this method.
        """
        pass

    def post_start_hook(self):
        """Hook to provide the manager the ability to do additional
        start-up work immediately after a service creates RPC consumers
        and starts 'running'.

        Child classes should override this method.
        """
        pass

    def reset(self):
        """Hook called on SIGHUP to signal the manager to re-read any
        dynamic configuration or do any reconfiguration tasks.
        """
        pass