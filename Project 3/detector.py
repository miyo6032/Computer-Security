#!/usr/bin/python3

import scapy
from scapy.all import *
from collections import defaultdict

if __name__ == '__main__':
    packets = rdpcap("proj3.dump.anon")

    # Final goal is to have a dictionary of ip addresses
    # with the count of syn packets sent and the count of syn_ack packet
    # received

    ip_packets = defaultdict(lambda: {"syn": 0, "synack": 0})
    
    for packet in packets:
        if(packet.haslayer(TCP)):
            tcp = packet[TCP]
            ip = packet[IP]
            syn_value = 2
            synack_value = 18
            
            if tcp.flags.value == syn_value:
                ip_packets[ip.src]["syn"]+=1
            
            elif tcp.flags.value == synack_value:
                ip_packets[ip.dst]["synack"]+=1

    for ip, counts in ip_packets.items():
        if counts["syn"] > 3 * counts["synack"]:
            print(ip)