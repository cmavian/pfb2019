#!/usr/bin/env python3

import sys
import re
import random



#fasta = sys.argv[2]
metadata = sys.argv[1]


fasta_dic = {}
#seq = ''


#make fasta as dictionary

#with open(fasta, 'r') as read_fasta:
#	for line in read_fasta:
#		line = line.rstrip()
#		if line.startswith('>'):# you find in the line starts with > assign the result to value of dictionary
#			seq = ''
#			group = re.search(r'^(>\S+)', line) # fasta_ID = '>'+key
#			key = group.group(1)
#			fasta_dic[key] = seq
#			print(key)
#		else: # concatanate each other line and assign to value
#			seq += line 
#			fasta_dic[key] = seq
#print(fasta_dic)


# read the metadata and add values to each key in the dictionary as a list
# [sequence, region, date]


line_list = []
meta = []
count_dict = {}

with open(metadata, 'r') as read_data:
	for row in read_data:
		row.replace('\r', '\n')
		row = row.rstrip()
		line_list = row.split(',')
		#line_list.append(ID)
		#line_list.append(region)
		#line_list.append(date)
		#print(line_list)
		if len(line_list) == 3:
			meta.append(line_list)
			country = line_list[1]
			if country in count_dict:
				previous_count = count_dict[country]
				new_count = previous_count +1
				count_dict[country] = new_count
			else:
				count_dict[country] = 1
#print(count_dict)
#print(list2)

#keep = []
#count_rec = {}

#for info in line_list:
	count_rec = count_dict[country] = [line_list[0],line_list[2]]



print(count_rec)

#for i in range(5):
#	rand_num = random.randint()
#	country = meta[rand_num] [1]
#	count_dict[country] +=1
#	if count_dict[country] > 2:
#		pass
#	else:
#		keep.append(meta[rand_num][0])

#print(keep-genes-ids)






	





