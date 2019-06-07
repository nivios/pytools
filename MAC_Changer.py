#!/usr/bin/env python

import subprocess

interface = "eth0"
mac = "00:11:22:33:44:55"

print("[+] Changing MAC address for " + interface + " to " + mac + ".")

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
