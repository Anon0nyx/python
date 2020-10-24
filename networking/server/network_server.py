#!/usr/bin/python3 
__author__ = 'Anon0nyx'

import socket

size = 512
host = ''
port = 6969

# Family = internet, type = stream. socket means TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# We have the socket, now we need to bind an IP address to this socket
# Along with a port
sock.bind((host, port))
sock.listen(5)

# We can store information about the other end
# Once we accept the connaction attempt
c, addr = sock.accept()
data = c.recv(size)
if data:
    f = open('storage.dat', '+a')
    print('Connection from: ', addr[0])
    f.write(addr[0])
    f.write(':')
    f.write(data.decode('utf-8'))
    f.close()
sock.close()
