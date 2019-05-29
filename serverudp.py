#!/usr/bin/python3

import socket, sys, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = int(sys.argv[1])

s.bind((host, port))

while True:
    mesg, addr = s.recvfrom(1084)
    mesg = mesg.upper()
    s.sendto(mesg,addr)