#!/usr/bin/python3
__author__='Anon0nyx'

import socket, time, sys
host='localhost'

my_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host, 6969)
try:
	my_socket.connect(addr) # To get this to work locally run nc -l 6969
	print("Connection Successful.")
	time.sleep(2)
except:
	print('Socket Connection Error.')
	my_socket.close()
	time.sleep(2)
	print('Socket Closed.')
	quit()

try:
    msg = b'hi, this is a client\n'
    my_socket.sendall(msg)
    print("Message Sent.")
    time.sleep(2)
except:
    print('Socket Communication Error.')
    quit()
finally:
    my_socket.close()
    print('Socket Closed.')
    time.sleep(2)
