# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:02:27 2018

@author: WolfWolf
"""
import random

user_input=input("provide your guess: ")

while user_input!= "exit":
    generated_num = random.randint(1,9)
    number_of_guesses = 1
    user_input=int(user_input)
    while generated_num != user_input:
        if user_input > generated_num:
            print("too high")
        else:
            print("too low")        
        number_of_guesses += 1
        print("actual num:",generated_num)
        user_input=int(input("provide your guess: "))
        
        
    print("generated number:",generated_num)    
    print("right guesses")
    print("number of attempts:", number_of_guesses)
    user_input=input("provide your guess: ")
