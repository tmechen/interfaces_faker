import random
import shlex
import socket
import subprocess

import yaml

with open(r'config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

for index, name in socket.if_nameindex():
    if name == config["interface"]:
        print("config for {name} before:".format(name=name))
        print("----------------------------------------------------")
        print(subprocess.call((shlex.split("ip addr show {name}".format(name=name)))))
        print("----------------------------------------------------")

        new_count = random.randint(1, config["max_ips"])
        print("adding {new_count} new ip adresses for {valid_lft} seconds".format(new_count=new_count,
                                                                                  valid_lft=config['valid_lft']))
        random_ips = sorted(random.sample(
            population=config['ip_range']['hosts'],
            k=new_count))
        for random_ip in random_ips:
            new_address = "{network}.{subnet}.{random_ip}/{CIDR}".format(
                network=config['ip_range']['network'],
                subnet=config['ip_range']['subnet'],
                random_ip=random_ip,
                CIDR=config['ip_range']['CIDR']
            )
            subprocess.call(

                shlex.split("ip addr add {new_address} dev {name} valid_lft {valid_lft} preferred_lft 0".format(
                    new_address=new_address,
                    name=name,
                    valid_lft=config['valid_lft'])))

        print("----------------------------------------------------")
        print("config for {name} after:".format(name=name))
        print(subprocess.call((shlex.split("ip addr show {name}".format(name=name)))))
        print("----------------------------------------------------")
