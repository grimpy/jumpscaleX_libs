from .crypto import encrypt_for_node

from Jumpscale import j
from .id import _next_workload_id


class ZDBGenerator:
    def __init__(self, explorer):
        self._nodes = explorer.nodes

    def create(self, reservation, node_id, size, mode, password, disk_type="SSD", public=False):
        """
        add a 0-db namespace workload to the reservation
        
        :param reservation: reservation where to add the volume
        :type reservation: tfgrid.workloads.reservation.1)
        :param node_id: id of the node where to reserve the volume
        :type node_id: str
        :param size: size of the namespace in GiB
        :type size: int
        :param mode: mode of the 0-db, can be 'seq' or 'user'
        :type mode: str
        :param password: password of the namespace. if you don't want password use a empty string
        :type password: str
        :param disk_type: type of disk,can be SSD or HDD
        :type str
        :param public: if public is True, anyone can write to the namespace without being authenticated
        :type public: bool, optional
        :return: newly created zdb workload
        :rtype: tfgrid.workloads.reservation.zdb.1
        """
        if disk_type not in ["SSD", "HHD"]:
            raise j.excpetions.Input("disk type can only be SSD or HDD")
        if mode not in ["seq", "user"]:
            raise j.excpetions.Input("mode can only be 'seq' or 'user'")

        zdb = reservation.data_reservation.zdbs.new()
        zdb.workload_id = _next_workload_id(reservation)
        zdb.node_id = node_id
        zdb.size = size
        zdb.mode = mode
        if password:
            node = self._nodes.get(node_id)
            zdb.password = encrypt_for_node(node.public_key_hex, password)
        zdb.disk_type = disk_type.lower()
        return zdb
