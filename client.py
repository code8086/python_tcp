#!/usr/bin/env python
import socket
host="localhost"
port=10000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.send("hello from client")
s.close()

