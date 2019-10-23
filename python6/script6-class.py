#!/usr/bin/env python3


seq = 'ACGTAGCTGACGATC'
seq_name = 'ABC1'
seq_origin = 'zika virus'


class DNA_record(object):
	def __init__(self, sequence, name, origin): # setting the attributes of my class: name, DNA sequence, organism
		self.sequence = sequence
		self.name= name
		self.origin = origin
	def len_method(self):  # setting the method to calculate the length of the sequence
		length = len(self.sequence)	
		return length   # important to set return to close the method definition
	def nt_comp(self):
		nt_composition = {}  # make a dictionary for nucleotide composition
		A_number = self.sequence.count('A')
		nt_composition['A_count'] = A_number
		T_number = self.sequence.count('T')
		nt_composition['T_count'] = T_number
		C_number = self.sequence.count('C')
		nt_composition['C_count'] = C_number
		G_number = self.sequence.count('G')
		nt_composition['G_count'] = G_number
		return nt_composition	
	def at_content(self):
		at = (((self.nt_comp()['A_count'] + self.nt_comp()['T_count'])/self.len_method())) # you can call the method in the next method by self.the_previous_method() and for the dictionary call the method() followed by [key]: dict_method()[key] 
		print(at)
		print(type(at))
		return at

	def gc_content(self):	
		gc = (((self.nt_comp()['G_count'] + self.nt_comp()['C_count'])/self.len_method()))
		return gc

obj = DNA_record(seq, seq_name, seq_origin)

print('My DNA is', obj.sequence, 'My DNA is called', obj.name, 'My DNA is from', obj.origin)
print('My DNA is', obj.len_method())  #remember to put () because it is using a method not calling attributes
#print('In DNA there are As:', obj.A_count(), 'In DNA there are Ts:', obj.T_count(), 'In DNA there are Gs:', obj.G_count(), 'In DNA there are Cs:', obj.C_count())
# I am going to write the upper in a simpler way 
print('In DNA there are As are {}, my Ts are {}, my Gs are {}, and my Cs are {}:'.format(obj.nt_comp()['A_count'], obj.nt_comp()['T_count'], obj.nt_comp()['G_count'], obj.nt_comp()['C_count'])) 

#remember extra parenthesis at the EOF for the print()
print('My AT content is {:.2%} and GC is {:.2%}'.format(obj.at_content(), obj.gc_content()))

#obj.at_content()

# make a dictionary instead for the nt_composition


