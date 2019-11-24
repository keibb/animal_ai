#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:19:45 2019

@author: keiji2
""" 
nov = [["","","","","","",""],
       ["","","","","","",""],
       ["","","","","","",""],
       ["","","","","","",""],
       ["","","","","","",""]]

for i in range(5):
    nov[0][i]= "_"
nov[0][5:7]=1,2
n = 3
for y in range(1,5):
    for x in range(7):
        nov[y][x]=  n
        n += 1
        
for w in range(len(nov)):
    print(nov[w])    
