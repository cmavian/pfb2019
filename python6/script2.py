#!/usr/bin/env python3

genes = {}

with open('Python_06.seq.txt', 'r') as read_file:	
	for line in read_file:
		line = line.rstrip()
		if line == '': #this is to get rid of the last empty line and it's empty value at the end \n\n
			continue
		gene_id,seq = line.split('\t')
		#gene_id = line[0] another way to define the key of my dictionary from the list
		#seq = line[1] another way to define the value of my dicionary from the list
		seq = seq[::-1]
		seq = seq.replace('C','g')
		seq = seq.replace('G','c')
		seq = seq.replace('T','a')
		seq = seq.replace('A','t')
		seq = seq.upper()
		genes[gene_id] = seq

