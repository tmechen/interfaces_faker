import subprocess

import ifcfg
import yaml

with open(r'config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

for name, interface in ifcfg.interfaces().items():
    print(name)
    if name == config["interface"]:
        print(subprocess.call([f"ip addr show {name}"]))
