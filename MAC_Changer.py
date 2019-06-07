#!/usr/bin/env python

# This is a simple python3 MAC address changer for Linux.

import subprocess

interface = input("interface > ")
mac = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + mac + ".")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])
