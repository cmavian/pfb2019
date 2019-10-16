#!/usr/bin/env python3


import sys 
import math

variable1 = int(sys.argv[1]) 
#this script doesn't work with strings, python recognizes every input as string and I am coverting it to numbers with int(), but only for numbers as input. 
print(type(variable1))

if bool(variable1) == True:
	message = 'True'
	print(message)
else:
	message = 'False'	
	print(message)

