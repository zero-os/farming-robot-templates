from js9 import j

from zerorobot.template.base import TemplateBase
from zerorobot.template.state import StateCheckError

class IPLease(TemplateBase):

    version = '0.0.1'
    template_name = "iplease"

    def __init__(self, name=None, guid=None, data=None):
        super().__init__(name=name, guid=guid, data=data)
        self.__ip = None
        # self.__timeout = None

    @property
    def info(self):
        """ Returns IPLease info 
        
        Returns:
            IPInfo -- ipinfo
        """
        pass


    def validate(self):
        pass

    def install(self):
        pass

    def uninstall(self):
        pass

