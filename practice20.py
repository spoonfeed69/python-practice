# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:04:50 2018

@author: WolfWolf
"""

import random

"""
generate a random sorted list
"""
num_of_elements=random.randint(10,15)

i=0
random_list=[]
while i < num_of_elements:
    random_list.append(random.randint(0,1000))
    i+=1
    
random_list.sort()

print("random list is: ",random_list)

input_num=int(input("provide your number: "))

search_list=random_list

is_in_list=False

while len(search_list) > 1:
    if input_num == search_list[int(len(search_list)/2)]:
        print("the number is in the list on position ", random_list.index(input_num))
        is_in_list=True
        break
    elif input_num > search_list[int(len(search_list)/2)]:
        search_list=search_list[int(len(search_list)/2):]
        
    else:
        search_list=search_list[:int(len(search_list)/2)]
        

if is_in_list == False:
    print("Your number is not in list")