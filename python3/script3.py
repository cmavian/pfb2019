#!/usr/bin/env python3

taxa = ('sapiens, erectus, neanderthalensis')
print(taxa)

#print second element in the variable that is a string, so it will be a 
print(taxa[1])
print(type(taxa))

#split the variable into individual words 
species = taxa.split(', ')
print(species)

#get the second element in the variable that is a list
print(species[1])
print(type(species))

#list alphabetically
print(sorted(species))

#list by length of each string
print(sorted(species, key=len))


