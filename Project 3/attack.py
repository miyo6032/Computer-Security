#!/usr/bin/python3

import scapy

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
    pass

def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__ == '__main__':
    main()
