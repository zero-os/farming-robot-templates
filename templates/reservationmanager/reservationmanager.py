from js9 import j

from zerorobot.template.base import TemplateBase
from zerorobot.template.state import StateCheckError
from j.clients.zos.sal.IPPoolManager import IPPoolsManager

class ReservationManager(TemplateBase):

    version = '0.0.1'
    template_name = "reservationmanager"

    def __init__(self, name=None, guid=None, data=None):
        super().__init__(name=name, guid=guid, data=data)
        self.validate()

    @property
    def pools_manager(self):
        return self._pools_manager
    
    def get_free_ip(self):
        pool_id, ip = self._pools_manager.get_any_free_ip()
        # should we create an iplease here?
        return pool_id, ip

    def release_ip(self, pool_id, ip):
        self._pools_manager(pool_id, ip)
        # here should we remove the iplease?

    def reserve_vm(self, cpu, memory):
        pass

    def reserve_gateway(self):
        pass

    def reserve_zdb_namespace(self, size, type):
        pass

    def validate(self):
        pools_names = self.data['pools']
        pools_sals = []
        for pool_name in pools_names:
            pool_service = self.api.services.get(name=pool_name)
            pools_sals.append(pool_service.pool)
        
        self._pools_manager = IPPoolsManager(pools=pools_sals)


    @property
    def info( self):
        pass
