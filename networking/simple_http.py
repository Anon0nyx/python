#!/usr/bin/python3
__author__ = "Anon0nyx"

import socket, re, http.client

h = http.client.HTTPConnection("www.udemy.com") # Create connection
h.request("GET", "/") # Make request
data = h.getresponse()
print(data.code)
print(data.headers)
text = data.readlines()

for i in text:
    print(i.decode("utf-8"))
