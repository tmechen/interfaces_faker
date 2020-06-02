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
        random_ips = sorted(random.sample(
            population=range(config["ip_range"]["min"], config["ip_range"]["max"] + 1),
            k=random.randint(1, config["max_ips"])))
        for random_ip in random_ips:
            new_address = f"{config['ip_range']['network']}.{random_ip}"
            print(new_address)
        # subprocess.call( shlex.split(f"ip addr add 192.168.4.244/23 dev {name} valid_lft {config['valid_lft']} preferred_lft 0"))
