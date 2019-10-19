#!/usr/bin/env python3

with open('Python_06.txt', 'r') as read_file, open('Python_06_uc.txt', 'w') as write_file:
	for line in read_file:
		new_file = (line.upper())
		#print(new_file)
		write_file.write(new_file + '\n')
		print(write_file)
