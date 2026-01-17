#!/usr/bin/env python3
import yaml
import json
import os

servers_dir = "data/servers"
inventory = {"_meta": {"hostvars": {}}}

all_group = {"hosts": [], "children": []}
inventory["all"] = all_group

for filename in os.listdir(servers_dir):
    if filename.endswith(".yml"):
        path = os.path.join(servers_dir, filename)
        with open(path) as f:
            data = yaml.safe_load(f)
            name = data["server_name"]
            all_group["hosts"].append(name)
            inventory["_meta"]["hostvars"][name] = {
                "ansible_host": data.get("public_ip", name),
                "ansible_user": data["ssh_user"],
            }

print(json.dumps(inventory))