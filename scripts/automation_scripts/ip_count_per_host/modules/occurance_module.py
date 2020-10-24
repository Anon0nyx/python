import csv, re

debug = False

def occurance(file_name):
	with open(str(file_name)) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		ip_addresses = {}
		count = 0
		pattern = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]', flags=0)
		for row in csv_reader:
			if count == 0:
				ip_addresses[row[2]] = [row[0]]
				if debug:
					#ip_addresses['Data Errors'] = []
					ip_addresses['Data Errors'] = 0
			elif pattern.match(row[2]):
				if row[2] not in ip_addresses:
					#ip_addresses[row[2]] = [row[0]]
					ip_addresses[row[2]] = 1
					continue
				else:
					ip_addresses[row[2]] += 1
					#if row[0] not in ip_addresses[row[2]]:
						#ip_addresses[row[2]].append(row[0])
						#continue
			else:
				if debug:
					ip_addresses['Data Errors'] += 1
					#ip_addresses['Data Errors'].append('1')
			count += 1
					
	return ip_addresses		
	
