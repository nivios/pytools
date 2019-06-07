#!/usr/bin/env python

import subprocess

interface = input("interface > ")
mac = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + mac + ".")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])
