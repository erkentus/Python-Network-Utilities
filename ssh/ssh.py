import sys
import socket
import argparse
import subprocess
import threading 

target = ""

def connect_ssh():
	global target
	print target

def main():
	global target

	parser = argparse.ArgumentParser()
	parser.add_argument('--target', '-t', help='ssh target IP', required=True)

	args = vars(parser.parse_args())
	target = args['target']

	connect_ssh()

main()