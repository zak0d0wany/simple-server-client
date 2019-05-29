#!/usr/bin/python3

import socket, sys

host = 'localhost'
port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    mesg = input("Write a message:")
    s.sendall(mesg.encode())
    if mesg=='q' or mesg=='Q':
        print("Connection closed")
        exit()
    else:
        feedback = s.recv(1024)
        print(feedback)
