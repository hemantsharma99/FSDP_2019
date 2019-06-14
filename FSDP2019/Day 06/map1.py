# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:37:26 2019

@author: admin
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
assign=map(lambda x: random.choice(code_names),names)
print(list(assign))
