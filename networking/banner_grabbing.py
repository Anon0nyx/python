#!/usr/bin/python3 
__author__ = 'Anon0nyx'

import socket, re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.google.com', 80))

http_get = b'GET / HTTP/1.1\nHost: www.google.com\n\n'
data = ''
debug = False

try:
    sock.sendall(http_get)
    data = sock.recvfrom(1024)
    print("Connection Successful\nData Collected")
except socket.error:
    print('Socket Error : ', socket.errno)
finally:
    print('Closing connection')
    sock.close()

str_data = data[0].decode('utf-8')
# Liiks like one long line so split it up at the newline chars
headers = str_data.splitlines()
if debug:
    print(headers)

# User regular expression library to look for the one line we want
for s in headers:
    if re.search('Server: ', s):
        s = s.replace('Server: ', '')
        print(s)
