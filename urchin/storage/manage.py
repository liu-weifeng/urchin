
class StorageManager(object):
    """

    """

    def __init__(self):
        pass

    def get_mtpaths(self):

        mtpaths = []
        file_name = "/proc/mounts"
        lines = file(file_name).readlines()
        for x in lines:
            xlst = x.strip().split()
            if len(xlst) != 6:
                continue
            if "/mnt/" not in xlst[1]:
                continue
            if xlst[1] not in mtpaths:
                mtpaths.append(xlst[1])
 
        return mtpaths

    def mount(self, param):
        """
        """
        mount_type = param['type']
        mount_path = param['mount_path']
        source = param['source']
        

    def umount(self):
        """
        shut down a instance
        :param name: instance name
        :return:
        """
        pass

