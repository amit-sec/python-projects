#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface", dest = "interface", help="Interface to change its MAC address")
	parser.add_option("-m","--mac", dest = "new_mac", help="New MAC Address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an interface , use --help")
	elif not options.new_mac:
		parser.error("[-] Please specify a new mac. use --help for more info")
	return options
		
def change_mac(interface, new_mac):
	print(" [+] Changing mac address for  " + interface + " and new mac is " + new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw","ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
	ifconfig_results = subprocess.check_output(["ifconfig", interface])
	mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)
	if mac_address:
		return mac_address.group(0)
	else:
		print("[-] could not read MAC Address[-]")
options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Curren MAC is = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
	print("[+] MAC Address was successfully change to " + current_mac)
else:
	print("MAC Address did not get changed")






