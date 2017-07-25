#!/usr/bin/python

#this program takes in a filename and a string which you want to search in that file
#spits out all the lines which has the occurrence of that particular string
#TO DO: 
#      Output logs searched by particular date
#
#Usage: 
# :#python logfinder.py <log filename>

import os
import string
import sys

def findstring(filename, stringname):
    with open(filename) as filetoberead:
		for linenum, line in enumerate(filetoberead, 1):
			if stringname in line:
				print linenum 
				print line
		else:
			print "String not Found!"

if __name__ == "__main__":
	# file_1 = raw_input("Enter the filename to look for logs: ")
	file_1 = sys.argv[1]
	word_1 = raw_input("Type the word you're looking for: ")
	findstring(file_1, word_1)
