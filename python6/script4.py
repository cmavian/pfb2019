#!/usr/bin/env python3

import sys
import re

fasta = sys.argv[1]

seq_list = []
id_list = []
#pattern = r"gi"

with open(fasta, 'r') as read_fasta:
	for line in read_fasta:
		line = line.rstrip()
		title = 
print(seq_list)
