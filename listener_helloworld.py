#!/usr/bin/env python3

import socket

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # basicaly allow to re-use socket
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connection")
        self.connection, self.address = listener.accept()
        print("[+] Got a connection from " + str(address))

    def execute_remotely(self, command):
        self.connection.send(command)
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = input(">> ")
            result = self.execute_remotely(command)
            print(result)

my_listener = Listener("192.168.204.128", 1234)
my_listener.run()


