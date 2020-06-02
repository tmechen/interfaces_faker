import ifcfg
import yaml
from pyroute2 import IPDB

with open(r'config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    print(config["interface"])

print(ifcfg.interfaces())

for name, interface in ifcfg.interfaces().items():
    if name == config["interface"]:
        print(interface)

    with IPDB() as ip:
        ip.interfaces[name]. \
            add_ip('172.16.0.1/24'). \
            add_ip('172.16.0.2/24'). \
            option('mtu', 1400). \
            up(). \
            commit()
