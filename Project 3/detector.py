#!/usr/bin/python3

import scapy
from scapy.utils import rdpcap

if __name__ == '__main__':
    a=rdpcap("proj3.pcap")
    print(a)