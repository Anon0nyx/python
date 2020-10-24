#!python3

'''
This widget script simply shows the current local IP address in a label.
'''

import appex, ui
import socket, re

def get_local_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(('google.com', 80))
		ip = s.getsockname()[0]
		s.close()
	except:
		ip = 'N/A'
	return ip
def get_global_ip():    
    url = "http://checkip.dyndns.org"    
    try:
        request = urllib.urlopen(url).read()
        ip = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)
    except:
        ip = 'N/A'
    return ip
    
label = ui.Label(font=('Menlo', 24), alignment=ui.ALIGN_CENTER)
label.text = 'Local IP: ' + get_local_ip()
label.text = 'Global IP: ' + get_global_ip()
appex.set_widget_view(label)
