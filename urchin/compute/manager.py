

class ComputeManager(object):
    """

    """

    def __init__(self):
        pass

    def start(self, name, storage_pool):
        """
        start a instance
        :param name: instance name like i-0000001
        :param storage_pool: storage pool which instance located
        :return:
        """
        pass

    def shut_down(self, name):
        """
        shut down a instance
        :param name: instance name
        :return:
        """
        self.power_off(name)

    def power_off(self, name):
        pass

    def sys_power_off(self, name):
        pass

    def reset(self, name):
        pass

    def sys_reboot(self, name):
        pass

    def snapshot(self, name):
        pass

    def attach_disk(self, name):
        pass

    def attach_nic(self, name):
        pass


