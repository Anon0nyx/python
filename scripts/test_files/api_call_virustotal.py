import requests
import json

clean = True
apikey = "526cbd4eb1cf07086aebdb65292e59bfbcb38c475b5e7c4054761ce01dbbed36"
domain = 'www.google.com'

post_url = 'https://virustotal.com/vtapi/v2/url/scan' # POST request
post_params = {'apikey': apikey, 'url': domain}

try: 
	# PART 1: Make POST request and queue scan
	resonse = requests.post(post_url, data=post_params) # Make initial POST request
	print(response)
	
	response = response.json() # Format this response
	
	data = json.dumps(response)
	data = json.loads(data)
	
	scan_id = data['scan_id'] # Aquire scan_id to access repot in GET request
	
	# Initialize GET variables
	get_url = 'https://virustotal.com/vtapi/v2/url/report'
	get_params = {'apikey': apikey, 'resource': scan_id}
	
	# PART 2: Make GET request and determine is domain is clean
	response = requests.get(get_url, data=get_params) # Send get request for report
	
	response.json() # Format
	
	scans = response['scans'] # Split up each individual report (There are many)
	
	for line in scans:
		if scans[line]['result'] != 'clean site' and scans[line]['result'] != 'unrated site':
			clean = False
	print("Site clean") if clean else print("Site NOT clean")
	
except Exception:
	print("Scan failed at execution: ", Exception)
	
