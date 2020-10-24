#!/usr/bin/python3
__author__ = "Anon0nyx"

import pcapy
from struct import *

cap = pcapy.open_live("en0", 65536, 1, 0)

while 1:
    (header, payload) = cap.next()
    l2hdr = payload[:14]
    l2data = unpack("!6s6sh", l2hdr)
    src_mac = "%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hrd[0]), ord(l2hrd[1]), ord(l2hrd[2]), ord(l2hrd[3]), ord(l2hrd[4]), ord(l2hrd[5]))
    dst_mac = "%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hrd[6]), ord(l2hrd[7]), ord(l2hrd[8]), ord(l2hrd[9]), ord(l2hrd[10]), ord(l2hrd[11]))
    print("Source MAC: ", src_mac, " Destination MAC: ", dst_mac)

    # Get IP header which is 20 bytes long
    # Unpace it into what it is 
    ip_header = unpack("!BBHHHBBH4s4s", payload[14:34])
    time_to_live = ip_header[5]
    protocol = ip_header[6]
    print("Protocol ", str(protocol), "Time To Live: ", str(time_to_live))
