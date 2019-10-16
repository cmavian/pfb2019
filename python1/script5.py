#!/usr/bin/env python3


import sys 
import math

number = int(sys.argv[1])

if number == 50:
	print('number equal to 50')
elif number > 0:
	if number < 50:
		print('positive and less than 50')
		if number%2 == 0:
			print('positive and less than 50 and even')
		else:
			print('positive and less than 50 and odd')
	else:
		print('positive and greater than 50')
	if number > 50:
		if number%3 == 0:
			print('it is larger than 50 and divisible by 3')
elif number == 0:
	print('number is 0')
else:
	print('negative')

