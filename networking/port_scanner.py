#!/usr/bin/pyton3
__author__ = "anon0nyx"

import socket

host = input("[**] Enter The Host To Scan: ")

def port_scanner(port):
    if sock.connect_ex((host, port)):
        print("Port %d is closed" % (port))
    else:
        print("Port %d is open" % (port))
    sock.close()

for i in range(1, 100):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_scanner(i)
