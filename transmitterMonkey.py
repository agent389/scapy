from scapy.all import *

def transmitterMonkey(packet):
	
    packet2 = IP(dst="224.3.0.1")/UDP(dport=1235, sport=1235)/packet

    send(packet2, iface = 'eth0')


sniff(filter="host 127.0.0.1 and udp port 1234", prn=transmitterMonkey)


