import random
import shlex
import subprocess

import ifcfg
import yaml

with open(r'config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

for name, interface in ifcfg.interfaces().items():
    if name == config["interface"]:
        print(f"config for {name} before:")
        print(f"----------------------------------------------------")
        print(subprocess.call((shlex.split(f"ip addr show {name}"))))
        print(f"----------------------------------------------------")
        for i in range(1, random.randint(1, config["max_ips"])):
            print(i)
