# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 08:46:18 2021

@author: Zulfiqar
"""

E = 'TEp'
Ep = '+TEp/@'
T = 'FTp'
Tp = '*FTp/@'
F = '(E)/id'



# print(f"The first of E' is {Ep[0]}")

def First(G):
    for i in range(len(G)):
        if (G[i] == '+' or G[i] == '*' or G[i+1] == 'id' or G[i] == '(' ):
            print(f'The ')
            
        
        
        