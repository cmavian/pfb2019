#!/usr/bin/env python3

import Bio
from Bio import SeqIO as SIO
from Bio.Seq import Seq as BS


for seq_record in SIO.parse('/Users/info/pfb2019/python6/zika_asian_clade_final_aln_101619.fa', 'fasta'):
	#print('ID',seq_record.id)
	print('Lenght', len(seq_record))
	line =0
	for line in seq_record:
		if line.startswith('>'):
			line +=1	
		print(line)  #WRONG!
