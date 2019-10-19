#!/usr/bin/env python3

#copy list by just putting list_copy = my_list

my_list = ['a', 'bb', 'ccc']
print(my_list)
list_copy = my_list
print(list_copy)

list_copy.append('dddd')
print(list_copy)
print(my_list)

# copy list with the funciton .copy()

my_list2 = ['a', 'bb', 'ccc']
print(my_list2)
list_copy2 = my_list2.copy()
print(list_copy2)

list_copy2.append('dddd')
print(list_copy2)
print(my_list2)


# Write a script that uses a while loop to print out the numbers 1 to 100


numbers = 0 

while numbers < 101:
	print('number:', numbers)
	numbers+= 1
print('Done')

# Write a script that uses a while loop to calculate the factorial of 1000.

num = 1
num2 =1
while num < 4:
	num+=1
	num2*=num
	print(num2, num)
print('Done')


# Iterate through each element of this list using a for loop

import math

num_var = [101,2,15,22,95,33,2,27,72,15,52]

for nums in num_var:
	if  nums % 2 == 0:
			print(nums)
print('Done')

for nums in num_var:
	print(nums)
print('Done again')

for nums in num_var:
	if nums % 2 == 0:
		print('these are even' , nums)
		nums + nums
	print('Sum of even numbers:', nums)
	elif nums % 2 == 1:
		nums += nums
		odd_nums = nums
	print('Sum of odd numbers:', odd_nums)

















