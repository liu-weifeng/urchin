

class Host(object):
    """
    libvirt connection
    hostname ...
    """

    def __init__(self):
        pass

    def get_connection(self):
        """
        get a connection to libvirt.
        :return:
        """
        pass

    def write_instance_config(self, xml):
        """
        Define and return a domain, bot does not start it.
        :param xml:
        :return: a domain instance
        """
        return self.get_connection().defineXML(xml)
