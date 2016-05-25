
from urchin.virt.libvirt import config as vconfig

class LibvirtDriver(object):

    def _get_guest_config(self):
        guest = vconfig.LibvirtConfigGuest()
        guest.virt_type = "kvm"
        guest.name = "test" # TODO: add name support
        guest.uuid = "test_uuid" # TODO: add uuid support
        guest.memory = 10 * 1024 # TODO: add memory support


