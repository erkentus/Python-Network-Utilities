import sys
import socket
import argparse
import subprocess
import threading

target = ""
port = None

def connect_to_server():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((target,port))
		while True:
			recv_len = 1
			response = ""
			while recv_len:
				data = client.recv(4096)
				recv_len = len(data)
				response += data
				if recv_len < 4096:
					break
			print response
			buffer = raw_input("")
			buffer += "\n";
			client.send(buffer)
	except Exception as ex:
		print str(ex)
		print "[*] Exception! Exiting."
		client.close()



def main():
	global target
	global port

	parser = argparse.ArgumentParser()
	parser.add_argument('--port', '-p', required=True)
	parser.add_argument('--target', '-t', help='target where netcat server is running', required=True)

	args = vars(parser.parse_args())
	target, port = args['target'], int(args['port'])
	connect_to_server()

main()