#!/usr/bin/env python

#coded during zaid sabih course on udemy
import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", dest = "ipaddr" , help = "Please specify ip address or ip range using -t ")
    (options, arguments) = parser.parse_args()
    if not options.ipaddr:
        parser.error("please specify ip address")
    return options
     

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
     
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    
    print("IP\t\t\tMac Address\n------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])
        
options = get_arguments()
scan_result = scan(options.ipaddr)
print_result(scan_result)






