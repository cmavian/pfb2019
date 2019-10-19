#!/usr/bin/env python3

import sys

fastq = sys.argv[1]




len_line = 0
count = 0
with open(fastq, 'r') as read_fastq:
	for line in read_fastq:
		count+=1
		len_line+=len(line)


print(count, 'total number of lines')
print(len_line, 'is the total number of characters')	
print(len_line//count, 'is the average line length')




