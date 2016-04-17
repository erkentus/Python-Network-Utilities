import sys
import socket
import argparse
import subprocess
import threading 

target = ""
port = None

def start_server():
	global target
	global port
	print target, port
	tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server.bind((target, port))
	tcp_server.listen(5) #backlog number http://linux.die.net/man/2/listen

	while True:
		client_socket, addr = tcp_server.accept()
		client_thread = threading.Thread(target=handle_client, args=(client_socket,))
		client_thread.start()

def handle_client(client_socket):
	while True:
		client_socket.send('$> ')
		cmd_buffer = ""
		while "\n" not in cmd_buffer:
			cmd_buffer += client_socket.recv(1024)
		response = run_cmd(cmd_buffer)
		client_socket.send(response)

def run_cmd(command):
	command = command.rstrip()
	try:
		output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
	except:
		output = "Failed to execute command.\r\n"
	return output

def main():
	global target
	global port

	parser = argparse.ArgumentParser()
	parser.add_argument('--port', '-p', help='port for server to listen', default=8001)
	parser.add_argument('--target', '-t', help='target to listen at', default='127.0.0.1')

	args = vars(parser.parse_args())
	target, port = args['target'], args['port']

	start_server()

main()