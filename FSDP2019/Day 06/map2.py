# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:49:46 2019

@author: admin
"""
def assign(x):
    x=hash(x)
    return x
names = ['Mary', 'Isla', 'Sam']
ass=map(assign,names)
print(list(ass))



