#!/usr/bin/python

# This program gives you back the number of logs generated over a period of time
# This time could be differentiated over a day, over an hour or a specific minute
# Use Case: You want to find out(count) how many lines of logs were written in a given specific time interval
# For simplicity, I took the logfile as a list and iterated over it by splitting it with delimiters

import re
import sys
import math
import datetime

# String manipulation
logfile = (
	"Feb 11 08:01:01 localhost systemd: Stopping user-0.slice.",
	"Feb 11 08:51:49 localhost dhclient[2899]: DHCPREQUEST on eth0 to 10.0.2.2 port 67 (xid=0x5ae19b1a)",
	"Feb 11 08:51:49 localhost dhclient[2899]: DHCPACK from 10.0.2.2 (xid=0x5ae19b1a)",
	"Feb 11 08:51:49 localhost NetworkManager[559]: <info>  [1518339109.2203] dhcp4 (eth0):   address 10.0.2.15",
	"Feb 11 08:51:49 localhost NetworkManager[559]: <info>  [1518339109.2205] dhcp4 (eth0):   plen 24 (255.255.255.0)",
	"Feb 11 08:51:49 localhost NetworkManager[559]: <info>  [1518339109.2206] dhcp4 (eth0):   gateway 10.0.2.2",
	"Feb 11 08:51:49 localhost NetworkManager[559]: <info>  [1518339109.2206] dhcp4 (eth0):   server identifier 10.0.2.2",
	"Feb 11 08:51:49 localhost NetworkManager[559]: <info>  [1518339109.2206] dhcp4 (eth0):   lease time 86400",
	"Feb 11 08:51:49 localhost NetworkManager[559]: <info>  [1518339109.2206] dhcp4 (eth0):   nameserver '10.0.2.3'",
	"Feb 11 08:51:49 localhost NetworkManager[559]: <info>  [1518339109.2206] dhcp4 (eth0):   domain name 'fios-router.home'",
	"Feb 11 08:51:49 localhost NetworkManager[559]: <info>  [1518339109.2206] dhcp4 (eth0): state changed bound -> bound",
	"Feb 11 08:51:49 localhost dbus[550]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service'",
	"Feb 11 08:51:49 localhost systemd: Starting Network Manager Script Dispatcher Service...",
	"Feb 11 08:51:49 localhost dbus-daemon: dbus[550]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service'",
	"Feb 11 08:51:49 localhost dhclient[2899]: bound to 10.0.2.15 -- renewal in 43119 seconds.",
	"Feb 11 08:51:49 localhost dbus[550]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'",
	"Feb 11 08:51:49 localhost dbus-daemon: dbus[550]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'",
	"Feb 11 08:51:49 localhost systemd: Started Network Manager Script Dispatcher Service.",
	"Feb 11 08:51:49 localhost nm-dispatcher: req:1 'dhcp4-change' [eth0]: new request (3 scripts)",
	"Feb 11 08:51:49 localhost nm-dispatcher: req:1 'dhcp4-change' [eth0]: start running ordered scripts...",
	"Feb 11 09:01:01 localhost systemd: Created slice user-0.slice.",
	"Feb 11 09:01:01 localhost systemd: Starting user-0.slice.",
	"Feb 11 09:01:01 localhost systemd: Started Session 95 of user root.",
	"Feb 11 09:01:01 localhost systemd: Starting Session 95 of user root.",
	"Feb 11 09:01:01 localhost systemd: Removed slice user-0.slice.",
	"Feb 11 09:01:01 localhost systemd: Stopping user-0.slice.",
	"Feb 11 09:01:01 localhost systemd: Starting Session 95 of user root.",
	"Feb 11 09:01:01 localhost systemd: Removed slice user-0.slice.",
	"Feb 11 09:01:01 localhost systemd: Stopping user-0.slice.",
	"Feb 11 10:01:02 localhost systemd: Created slice user-0.slice.",
	"Feb 11 10:01:02 localhost systemd: Starting user-0.slice.",
	"Feb 11 10:01:02 localhost systemd: Started Session 96 of user root.",
	"Feb 11 10:01:02 localhost systemd: Starting Session 96 of user root.",
	"Feb 11 10:01:02 localhost systemd: Removed slice user-0.slice.",
	"Feb 11 10:01:02 localhost systemd: Stopping user-0.slice."
)

# Create an empty hashmap to store the kv pairs
OutputMinutes = {}

# for i in open("/var/log/messages","r"):
for i in logfile:
	#Sort messages by splitting the string
  minute = ":".join(i.split(":")[:2])
	# print minute
	if minute not in OutputMinutes:
		OutputMinutes[minute] = 1
		# print OutputMinutes
	else:
		OutputMinutes[minute] += 1
# print OutputMinutes
# print "\n"

for minute in sorted(OutputMinutes):
  # print OutputMinutes
	print '%s, %s' %(minute, OutputMinutes[minute])
