# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:00:22 2021

@author: Zulfiqar
"""

file = open("code_with_comments.py","r") #reading file
            
    
# l=file.readlines() # reading line by line using readlines method
# countsingle=[] # empty list for counting single comment
# countdouble=[] # empty list for counting multi comment
# for i in range(len(l)): #for loop on list of contents
#     if(l[i][0]=='#'): # checking if there is single comment 
#         countsingle.append(i+1) # appending the conunt for single comment
#     if(l[i][0:3]=='\""\"'): # checking if there is single comment 
#         countdouble.append(i+1) # appending the conunt for single comment
        
# for i in range(len(counts++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ingle)): # for loop on list countsingle
#     print("single line comment at ",countsingle[i]) # printing line number of single comment
# for i in range(len(countdouble)): # for loop on list countdouble
#     print("Multi-line line comment at ",countdouble[i]) # printing line number of multiplecomment

        
# l=file.readlines()

countsingle=[]
countdouble=[] 
# for i in range(len(l)):
#     for j in range(len(list(i))):
#         if(l[i][j]=='#'): 
#             countsingle.append(i) 
#         # if(l[i][j]=='\""\"'):  
#         #     countdouble.append(i+1) 
        
# for i in range(len(countsingle)): # for loop on list countsingle
#     print("single line comment at ",countsingle[i]) # printing line number of single comment
# for i in range(len(countdouble)): # for loop on list countdouble
#     print("Multi-line line comment at ",countdouble[i]) # printing line number of multiplecomment
for line in file:
    for ch in line:
        if ch == '#':
            countsingle.append(line) 
        
for i in range(len(countsingle)): # for loop on list countsingle
    print("single line comment at ",countsingle[i]) # printing line 