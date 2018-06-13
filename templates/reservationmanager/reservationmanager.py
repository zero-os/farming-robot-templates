from js9 import j

from zerorobot.template.base import TemplateBase
from zerorobot.template.state import StateCheckError

class ReservationManager(TemplateBase):

    version = '0.0.1'
    template_name = "reservationmanager"

    def __init__(self, name=None, guid=None, data=None):
        super().__init__(name=name, guid=guid, data=data)

    def get_free_ip(self):
        pass

    def reserve_vm(self, cpu, memory):
        pass

    def reserve_gateway(self):
        pass

    def reserve_zdb_namespace(self, size, type):
        pass

    def validate(self):
        pass

    @property
    def info( self):
        pass
