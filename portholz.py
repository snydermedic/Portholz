#!/usr/bin/python
import socket
import subprocess
import sys
from datetime import datetime

remServ = raw_input('Enter a remote host to scan: ')
remServIP = socket.gethostbyname(remServ)

print "Scanning..."

try:
    for port in range (1,1025):
        soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        out = soc.connect_ex((remServIP, port))
        if out == 0:
            print "Port {}  OPEN".format(port)
        soc.close()

except socket.gaierror:
    print "Host not resolved"
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()
