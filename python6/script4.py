#!/usr/bin/env python3

import sys
import re

fasta = sys.argv[1]

fasta_dic = {}
value = ''

with open(fasta, 'r') as read_fasta:
	for line in read_fasta:
		line = line.rstrip()
		if line.startswith('>'):# you find in the line starts with > assign the result to value of dictionary
			value = ''
			key = re.search(r'^>(\S+) (.\S.+)', line) # fasta_ID = '>'+key
			geneID = key.group(1)
			fasta_dic[geneID] = value
			print(geneID)
		else: # concatanate each other line and assign to value
			value += line 
			fasta_dic[geneID] = value

print(fasta_dic)
