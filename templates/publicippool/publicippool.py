from js9 import j
import ipaddress
from zerorobot.template.base import TemplateBase
from zerorobot.template.state import StateCheckError
from j.clients.zos.sal.IPPoolManager import IPPool, _as_ip4


def fmt_ip2lease(ipaddr):
    ip = _as_ip4(ipaddr)
    return "lease_{}".format(int(ip))

def int2ip(n):
    return str(ipaddress.IPv4Address(n))

def ip_from_leasename(leasename):
    # lease_ipnumber
    ipnumber = int(leasename.split("_")[1])
    return int2ip(ipnumber)
    
class PublicIPPool(TemplateBase):

    version = '0.0.1'
    template_name = "publicippool"

    def __init__(self, name=None, guid=None, data=None):
        super().__init__(name=name, guid=guid, data=data)
        self.validate()

    def validate(self):
        pool_id = self.data['id']
        network_id = self.data['networkId']
        subnet_mask = self.data['subnetMask']
        name = self.data['name']
        ips = self.data['ips']
        networkaddr = ipaddress.IPv4Network(network_id)
        networkaddr.netmask = subnet_mask
        # TODO: support constructing network address from subnet mask not only the cidr.
        networkaddr = str(networkaddr)
        self._pool = IPPool(id=pool_id, name=name, network_address=network_id, registered_ips=ips)
    
    @property
    def pool(self):
        return self._pool

    def reserve_ip(self):
        ip = self._pool.get_free_ip()
        ipdecimal = int(ip)
        self._pool.reserve_ip(ip)
        iplease_service = self.api.services.create("github.com/zero-s/farming-robot-templates/0.0.1","iplease_{}".format(ipdecimal) )
        iplease_service.schedule_action('install').wait(die=True)

    def release_ip(self, ipaddr):
        iplease_service_name = fmt_ip2lease(ipaddr)
        iplease_service = self.api.services.get(name=iplease_service_name)
        self._pool.release_ip(ipaddr)
        iplease_service.schedule_action('uninstall').wait(die=True)
        iplease_service.delete()

    def uninstall(self):
        for ip in self._pool.reserved_ips:
            self.release_ip(ip)





