import sys
import os
import socket
import struct
from ctypes import *

class IP(Structure):
	_fields_ = [ #https://docs.python.org/2/library/ctypes.html @ 15.17.1.10-12
		("ihl", c_ubyte, 4),
		("version", c_ubyte, 4),
		("tos", c_ubyte),
		("len", c_ushort),
		("id", c_ushort),
		("offset", c_ushort),
		("ttl", c_ubyte),
		("protocol_num", c_ubyte),
		("sum", c_ushort),
		("src", c_uint32),
		("dst", c_uint32)
	]
	def __new__(self, socket_buffer=None):
		# This method creates a ctypes instance, copying the buffer from the source object 
		# buffer which must be readable. 
		# The optional offset parameter specifies an offset into the source buffer in bytes; 
		# the default is zero. If the source buffer is not large enough a ValueError is raised.
		return self.from_buffer_copy(socket_buffer)
	def __init__(self, socket_buffer=None):
		self.protocol_map = {1:"ICMP", 6: "TCP", 17: "UDP"}
		# Convert a 32-bit packed IPv4 address (a string four characters in length) 
		# to its standard dotted-quad
		# string representation (for example, 123.45.67.89
		self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
		self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))
		try:
			self.protocol = self.protocol_map[self.protocol_num]
		except Exception as ex:
			print ex
			self.protocol = str(self.protocol_num)

