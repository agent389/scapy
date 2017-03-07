from scapy.all import *

def recieverMonkey(packet):
	
    packet2 = packet[Raw]
    packet2.show()
    sendp(packet2, iface = 'eth0')


sniff(filter="host 224.3.0.1 and udp port 1235", prn=recieverMonkey)


