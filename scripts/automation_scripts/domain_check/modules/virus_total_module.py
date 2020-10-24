import json, requests
def check(domain):
	clean = True
	apikey = '526cbd4eb1cf07086aebdb65292e59bfbcb38c475b5e7c4054761ce01dbbed36'
	
	post_url = 'https://virustotal.com/vtapi/v2/url/scan'
	post_params = {'apikey': apikey, 'url': domain}

	response = requests.post(post_url, data=post_params)	

	response = response.json()
	data = json.dump(response)
	data = json.load(data)
	print(data)
	scan_id = data['scan_id']


	get_url = 'https://virustotal.com/vtapi/v2/url/report'
	get_params = {'apikey': apikey, 'resource': scan_id}

	response = requests.get(get_url, data=get_params)

	response = response.json()


	scans = response['scans']
	
	for line in scans:
		if scans[line]['result'] != 'clean site' and scans[line]['result'] != 'unrated site':
			clean = False
			
	return True if clean == True else False
		
		
