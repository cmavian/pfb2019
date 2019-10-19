#!/usr/bin/env python3

fav_list = ['dog', 'mezcal', 'basil', 'fries', 'art']

print(fav_list)

print(fav_list[2]) 

fav_list.pop(2)

new_list_pop = fav_list.copy()
print(new_list_pop)

new_list_pop.insert(2,'mint')

new_list = new_list_pop.copy()
print(new_list)


new_list.append('garage music')
print(new_list)

new_list.insert(0,'road bike')
print(new_list)


new_list.insert(3,'sunshine')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.pop(4)
print(new_list)

sentence = ' '.join(new_list)
print(sentence)

