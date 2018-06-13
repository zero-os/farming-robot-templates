from js9 import j

from zerorobot.template.base import TemplateBase
from zerorobot.template.state import StateCheckError

class PublicIPPool(TemplateBase):

    version = '0.0.1'
    template_name = "publicippool"

    def __init__(self, name=None, guid=None, data=None):
        super().__init__(name=name, guid=guid, data=data)

    def get_free_ip(self):
        pass

    def release_ip(self, iplease):
        pass

    def validate(self):
        pass

    def install(self):
        pass

    def uninstall(self):
        pass





