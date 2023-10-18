#! /usr/bin/env python3

import os

from dotenv import load_dotenv
from netmiko import ConnectHandler

load_dotenv()

host = os.environ['ROUTER']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

device = ConnectHandler(host=host,
                        username=username,
                        password=password,
                        device_type="cisco_xe",
                        )

output = device.send_command("show version")

print(output)
