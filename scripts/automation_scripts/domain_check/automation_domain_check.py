import requests, json, time, sys
from modules import virus_total_module
def main(file):
	try: 
		read_file = open(str(file), 'r')
	except:
		print("File Does Not Exist")
	try:
		write_file = open('bad_domain_list.txt', 'w+')
	except:
		print("File For Bad Domain List MISSING")
	
	for domain in read_file:
		domain = domain.strip('\n')
		result = virus_total_module.check(domain)
		print('[ ', domain, ' ] is clean (According to: virustotal)') if result == True else print('[ ', domain, ' ] is not clean (According to: virustotal)')	
		print(result)
	
	print('\nDomain Scanning is Complete\n')
	read_file.close()
	write_file.close()
	
if __name__ == '__main__':
	main('domain_list.txt')
	#main(input("Enter File: "))
	# OR
	# main(sys.argv[1])
	# If you are calling from the command line
