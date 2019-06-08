#!/usr/bin/env python

# A simple python3 MAC address changer for Linux.

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest ="interface", help="Interface that will have its MAC address changed.")
parser.add_option("-m", "--mac", dest ="mac", help="New MAC address for the specified interface.")

(options, arguments) = parser.parse_args()

interface = options.interface
mac = options.mac

print("[+] Changing MAC address for " + interface + " to " + mac + ".")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])
