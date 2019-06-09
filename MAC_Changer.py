#!/usr/bin/env python

# A simple python3 MAC address changer for Linux.

import subprocess
import optparse


def get_arguements():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface that will have its MAC address changed.")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address for the specified interface.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.mac:
        parser.error("[-] Please specify a MAC address, use --help for more info.")
    return options



def change_mac(interface, mac):
    print("[+] Changing MAC address for " + interface + " to " + mac + ".")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguements()
change_mac(options.interface, options.mac)
