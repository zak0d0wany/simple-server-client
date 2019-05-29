#!/usr/bin/python3

import socket, sys, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = int(sys.argv[1])

while True:
    msg = input("Type a message: ")
    s.sendto(msg.encode(),(host,port))
    feedback, addr = s.recvfrom(1024)
    print(feedback.decode())