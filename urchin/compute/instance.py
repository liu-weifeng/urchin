

# TODO: complate it
class Disk(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')


class Nic(object):
    def __init__(self, **kwargs):
        self.mac = kwargs.get('mac')
        self.name = kwargs.get('name')
        self.pci = kwargs.get('pci')


class Instance(object):

     def __init__(self, **kwargs):

         self.name = kwargs.get('name', None)
         self.mem = kwargs.get('mem', 1024) * 1024
         self.cpus = kwargs.get('cpus', 1)
         self.disks = kwargs.get('disks')