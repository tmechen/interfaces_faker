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

        new_count = random.randint(1, config["max_ips"])
        print(f"adding {new_count} new ip adresses")
        random_ips = sorted(random.sample(
            population=range(config["ip_range"]["min"], config["ip_range"]["max"] + 1),
            k=new_count))
        for random_ip in random_ips:
            new_address = f"{config['ip_range']['network']}.{random_ip}"
            subprocess.call(
                shlex.split(f"ip addr add {new_address} dev "
                            f"{name} valid_lft {config['valid_lft']} "
                            f"preferred_lft 0"))
            
        print(f"----------------------------------------------------")
        print(f"config for {name} after:")
        print(subprocess.call((shlex.split(f"ip addr show {name}"))))
        print(f"----------------------------------------------------")
