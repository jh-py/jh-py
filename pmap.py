#!/bin/python3

#importing modules.
import time
import sys
import nmap
from datetime import datetime
import pyfiglet as pfg

#Setting Variables.
N = nmap.PortScanner()
B =pfg.figlet_format("WELCOME TO PMAP!")
S = time.sleep(3)
Ip = sys.argv[1]

#Define who the target is.
if len(sys.argv) == 2:
	T = N.scan(sys.argv[1], '20-80') 
else:
	print("Argument Invalid")
	print("syntax: python3 pmap.py <ip>")
S
#Welcome introduction.
print(B)
	
#Banner.
S
print('_' * 50)
print('=' * 50)
print('scanning target: ')
print(Ip)
print('=' * 50)
print('Time Started: '+str(datetime.now()))
print('_' * 50)
S

#Scanning the target port.
	
for host in N.all_hosts():
     print('Host : %s (%s)' % (host, N[host].hostname()))
     print('State : %s' % N[host].state())
     for proto in N[host].all_protocols():
         print('-' * 50)
         print('Protocol : %s' % proto)
 
         lport = N[host][proto].keys()
         sorted(lport)
         for port in lport:
             print ('port : %s\tstate : %s' % (port, N[host][proto][port]['state']))
print('-' * 50)
