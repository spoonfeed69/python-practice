# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:16:43 2018

@author: WolfWolf
"""

while(True):
    player1_input=input("player 1 input: ")
    player2_input=input("player 2 input: ")
    game_dict={"rock": 1, "scissors": 2, "paper": 3}
    
    result_score = game_dict[player1_input] - game_dict[player2_input]
    
    """player 1 winning score: 
        1 - 2 = -1
        2 - 3 = -1
        3 - 1 = 2
        player 2 winning score:
        1 - 3 = -2
        2 - 1 = 1
        3 - 2 = 1
        """
    if result_score == -1 or result_score == 2:
        print("player 1 wins")
    else:
        print("player 2 wins")
        
    continue_reply=input("do you want to continue? [y/n]: ")
    
    if continue_reply=="y":
        continue
    else:
        break