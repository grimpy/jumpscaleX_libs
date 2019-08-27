from Jumpscale import j
from sal.kvm.Network import Network
from sal.kvm.Interface import Interface
from sal.kvm.Disk import Disk
from sal.kvm.Pool import Pool
from sal.kvm.StorageController import StorageController
from sal.kvm.KVMController import KVMController
from sal.kvm.Machine import Machine
from sal.kvm.CloudMachine import CloudMachine
from sal.kvm.MachineSnapshot import MachineSnapshot

JSBASE = j.baseclasses.object


class KVM(j.baseclasses.object):
    __jslocation__ = "j.sal.kvm"

    def _init(self, **kwargs):
        self.__imports__ = "libvirt-python"
        self.KVMController = KVMController
        self.Machine = Machine
        self.MachineSnapshot = MachineSnapshot
        self.Network = Network
        self.Interface = Interface
        self.Disk = Disk
        self.Pool = Pool
        self.StorageController = StorageController
        self.CloudMachine = CloudMachine
