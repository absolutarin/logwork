#!/usr/bin/python

# - Create a tool to find the IP address, Hostname and Domain. 
# This program logs in to servers through IP address and passes in
# Public Key for secure auth. Once logged in, grabs the hostname and 
# maps that to the IP address used. 
# Ideal situation would be to create a text file with all the mappings
# TO DO: 
#       Map all Hostnames to Domains
#
# Domain names can be found under /local/domains/<domain>

# - Create a hashmap for IP and Hostname :: KV pair
# - Create a hashmap for Hostname and Domain :: KV pair
# - Map both hashmaps to a text file

import os
import sys
import string

def maphostname(ipaddr):
	print "voila!"
	temphost = []
	if ipaddr is None:
		print "Check the IP Address"
	else:
		for i in ipaddr:
		    os.system("ssh root@ipaddr -i ~/.ssh/mysshkey020")
		    temphost = os.system("hostname")
		    os.system("exit")
		host2lst = list(temphost)
		templistcomp = (ipaddr, host2lst)
		print templistcomp


if __name__ == '__main__':
	iparg = sys.argv[1]
	maphostname(iparg)
