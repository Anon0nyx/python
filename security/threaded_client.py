#!/usr/bin/python3
__author__ = "Anon0nyx"

import socket, threading
# import urllib2 # Must install urllib2 

class clientConnect(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = ("www.google.com", 443)
        sock.connect(addr)
        print("Connection Established\n")

sock_clients = []
for i in range(1 ,6):
    s = clientConnect()
    s.start()
    print("[ Started: ", i, " ]\n", sep="")
    sock_clients.append(s)
