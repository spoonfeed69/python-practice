# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:19:11 2018

@author: WolfWolf
"""

from practice26 import determine_winner

def is_dead(data):
    result_list=[]
    result_list.append(data[0])
    result_list.append(data[1])
    result_list.append(data[2])
    result_list.append([data[0][0],data[1][1],data[2][2]])
    result_list.append([data[0][2],data[1][1],data[2][0]])
    result_list.append([data[0][0],data[1][0],data[2][0]])
    result_list.append([data[0][1],data[1][1],data[2][1]])
    result_list.append([data[0][2],data[1][2],data[2][2]])
    for i in result_list:
        eval_str=""
        for j in i:
            eval_str+=str(j)
        if len(eval_str.strip("0")) == 1 or len(eval_str.strip("0")) == 0:
            return False
    return True

print("game starts")
game_over=False
board=[[0,0,0],[0,0,0],[0,0,0]]

player=1

while game_over==False:
    
    player_input=input("player  input: ")
    player_input_location=[]
    for i in player_input.split(","):
        player_input_location.append(int(i)-1)
    
    if board[player_input_location[0]][player_input_location[1]] != 0:
        print("You cannot write on this position")
    else:
        if player==1:
            board[player_input_location[0]][player_input_location[1]]="x"
            player=2
        else:
            board[player_input_location[0]][player_input_location[1]]="o"
            player=1
        
    for i in board:
        print(i)
    
    if is_dead(board) == True:
        print("No more available moves")
        game_over=True
    elif determine_winner(board) != 0:
        if determine_winner(board) == {'x'}:
            print("player 1 wins")
        else:
            print("player 2 wins")
        game_over=True
      