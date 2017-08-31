#!/usr/bin/python

# This python program prints all the application version on a curl request
# A JSON file contains all the IPs of all the servers, names (not hostname)
# under each enviromment and a list of microservices running under each web domain
# 
# json filename: domainparser.json
# 
# Execute http://ipAddr/portNumber/microservices
#

import os
import sys
import json

def runtest():
	with open('applist.json') as json_data:
		d = json.load(json_data)
		print d
		# for key,value in d.items():
		# 	if key=="domain":
		# 		print key,value

# WORK IN PROGRESS #

if __name__ == '__main__':
	runtest()
