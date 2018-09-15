# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:43:53 2018

@author: WolfWolf
"""

input_list=input("input your series of numbers with space in between: ")

criteria = int(input("Input your criteria: "))

input_list=input_list.split(" ")

num_list = []

for x in input_list:
    
    if int(x) < criteria:
        num_list.append(int(x))

print(num_list)    

