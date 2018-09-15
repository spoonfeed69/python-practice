# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:42:16 2018

@author: WolfWolf
"""

input_num=int(input("Provide your number: "))

divisor_range=range(2 , int(input_num/2)+1)

divisor_list=[]

for divisor in divisor_range:
    if input_num % divisor == 0:
        divisor_list.append(divisor)

print("Your divisor list is: " + str(divisor_list))