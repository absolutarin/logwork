#!/usr/bin/python

# The purpose of this script is to find the most occuring log text from a bunch of log files
# The log files consists of a heterogenous collection of elements, both char and int combined. 
# Goal is to find the highest occuring element, for e.g. ERROR or SEVERE or FAULT, and sort 
# them in a descending order to the least occuring element

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vulputate nisl ex, et pellentesque ante aliquam a. Nullam id odio bibendum enim tempor aliquet id vel enim. Mauris pretium auctor lobortis. Morbi a posuere erat, quis finibus leo. Praesent fringilla cursus accumsan. Sed eget vestibulum eros. Mauris sollicitudin sed mi nec condimentum. Aliquam facilisis metus quis felis blandit consequat id sit amet urna. Donec pellentesque augue sed massa aliquet, sed pulvinar purus gravida. Pellentesque vestibulum, orci vitae pellentesque imperdiet, quam purus semper nulla, a bibendum erat mi sed quam. Cras interdum metus id metus pharetra aliquet. Aliquam sed facilisis nisi, at pellentesque quam. Ut imperdiet ullamcorper orci et vestibulum."

import os
import random
import string

def counttext():
	newstr = text.translate(None, string.punctuation)	#remove all punctuations,.' and create a new str
	newstr = newstr.split()		#split that string by whitespace
	newlist = list(newstr) 		#convert string into list

	emptylist = []

    for allitems in newlist:
		if 	allitems==allitems:
			out1= newlist.count(allitems)
			out2= allitems
			# print out1,":",out2
			finalstring = str(out1) + "_" + out2 
			# print finalstring
			emptylist += finalstring.split()

  print "Unsorted list: \n", emptylist
	print "\n"
	
  #Sorting from most to least
  print "Sorted list is: \n", sorted(emptylist, reverse=True)

if __name__ == '__main__':
	counttext()
