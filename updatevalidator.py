#!/usr/bin/python

# This tool logs in to each server and finds the port number
# which the OS update application listens on. 
# Make a note of the ip address as well
# Return the response as "IP Address:Port"
# netstat -plant | grep 2289
# ifconfig eth0 | grep inet | awk {'print $2'} | sed -e 's/addr://g'
# 
# To be continued...
