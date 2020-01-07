#!/usr/bin/python3

import os
import json
import time

user = os.getenv("SUDO_USER")

if user is None:
    print("run this with sudo !!!!")
    exit()

installation_packages = json.load(open('Packages.json'))

os.system("sudo apt update  ")
os.system("sudo apt upgrade -y --allow-downgrades")

for packages in installation_packages:

    os.system("sudo apt install %s -y"%(packages))

time_end = time.time() + 11
os.system("figlet 'Your system will reboot in 10 Seconds press Ctrl+c to stop the reboot' ")

while time.time() < time_end:
    yes = True

os.system("figlet Yes Bye")
os.system("reboot")
