#!/usr/local/bin/python3 

import ftplib

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous','anonymous')
		print('[*]' + str(hostname) + ' FTP Anonymous Login Succeeded.')
		ftp.quit()
		return True
	except Exception:
		print('[-]' + hostname + 'FTP Anonymous Login Failed')

host = input('[*]Enter Host Address: ')
anonLogin(host)
