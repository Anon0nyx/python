#!/usr/bin/python3 
__author__ = "Anon0nyx"

import pcapy

devs = pcapy.findalldevs()
print(devs)

cap = pcapy.open_live("en0", 65536, 1, 0) 

count = 1
while count:
    (header, payload) = cap.next()
    print(count)
    count-=-1

