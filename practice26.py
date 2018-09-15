# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:01:21 2018

@author: WolfWolf
"""

def determine_winner(data):
    winner=0
    result_list=[]
    result_list.append(set(data[0]))
    result_list.append(set(data[1]))
    result_list.append(set(data[2]))
    result_list.append(set([data[0][0],data[1][1],data[2][2]]))
    result_list.append(set([data[0][2],data[1][1],data[2][0]]))
    result_list.append(set([data[0][0],data[1][0],data[2][0]]))
    result_list.append(set([data[0][1],data[1][1],data[2][1]]))
    result_list.append(set([data[0][2],data[1][2],data[2][2]]))

    for i in result_list:
        if len(i) == 1 and next(iter(i))!=0:
            winner=i
    
    return winner
