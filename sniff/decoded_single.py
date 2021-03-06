import sys
import socket
import os
# python class implementation of the IP header 
from IPHeader.header import *

def get_host():
	return socket.gethostbyname(socket.gethostname())

def is_windows():
	return "nt" in os.name

def sniff_network():
	host = get_host()
	if is_windows(): socket_protocol = socket.IPPROTO_IP
	else: socket_protocol = socket.IPPROTO_ICMP
	# SOCK_RAW - access ip packet directly (IP protocol)
	# IPPROTO_IP - on Windows all types of packets
	# IPPROTO_ICMP - on Linux only ICMP packets can be sniffed
	sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
	sniffer.bind((host, 0))
	# include IP headers #http://linux.die.net/man/2/setsockopt
	sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	# https://msdn.microsoft.com/en-us/library/ms741621%28VS.85%29.aspx
	if is_windows(): sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON) #promiscuous mode
	try:
		while True:
			raw_buffer = sniffer.recvfrom(65565)[0]
			ip_header = IP(raw_buffer)
			print "Protocol: %s %s -> %s" % (ip_header.protocol, ip_header.src_address, 
				ip_header.dst_address)
	except KeyboardInterrupt:
		if is_windows(): sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

def main():
	sniff_network()

main()