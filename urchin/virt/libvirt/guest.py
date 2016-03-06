import libvirt


class Guest(object):

    def __init__(self, domain):

        self._domain = domain

    def __repr__(self):
        return "<Guest %(id)d %(name)s %(uuid)s>" % {
            'id': self.id,
            'name': self.name,
            'uuid': self.uuid
        }

    @property
    def id(self):
        return self._domain.ID()

    @property
    def uuid(self):
        return self._domain.UUIDString()

    @property
    def name(self):
        return self._domain.name()

    @classmethod
    def create(cls, xml, host):
        """
        Create a new guest
        :param xml:
        :param host:
        :return:
        """
        domain = host.write_instance_config(xml)

        return cls(domain)

    def launch(self, pause=False):
        """Starts a created guest.

        :param pause: Indicates whether to start and pause the guest
        """
        flags = pause and libvirt.VIR_DOMAIN_START_PAUSED or 0
        try:
            return self._domain.createWithFlags(flags)
        except Exception:
            pass

    def power_off(self):
        """Stops a running guest."""
        self._domain.destroy()

    def resume(self):
        """Resumes a suspended guest."""
        self._domain.resume()
