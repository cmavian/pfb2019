#!/usr/bin/env python3

# to run ./BLAST_script.py blast*.txt  because it has a for loop to run many files

import sys
import re

hit_files = []

field_str = 'qseqid, sseqid, percid, alen, mismat, gaps, q_start, q_end, s_start, s_end, evalue, bits'
fields = field_str.split(', ')

hitlist = []


for hit_file in  sys.argv[1:]:  # : opens all files 

	with open(hit_file, 'r') as fin:
		for line in fin:
			if line[0]=='#':
				continue
			hit_data = dict(zip(fields, line.strip('\n').split('\t')))
			hit_data['file'] = hit_file
			hitlist.append(hit_data)
			break

for hit in hitlist:
	print('\t'.join([hit[x] for x in ('file','percid','alen','evalue')]))

