#!/usr/bin/python3

import socket, sys, os

host = socket.gethostname()
port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',port))

s.listen(1)

while True:
    c, addr = s.accept()
    newpid = os.fork()
    if newpid == 0:
        while True:
            mesg = c.recv(1024)
            if mesg == b"q" or mesg == b"Q":
                print("Killing connection ", os.getpid())
                exit()
            else:
                c.sendall(b"Hi!" + mesg)
