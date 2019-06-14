# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:58:08 2019

@author: admin
"""
people = [{'name': 'Mary', 'height': 160},{'name': 'Isla', 'height': 80},{'name': 'Sam'}]
from functools import reduce
height_total = reduce(lambda a,b:a+ b,map(lambda y:y['height'],filter(lambda x: 'height' in x,people)))
height_count=len(list(filter(lambda x: 'height' in x,people)))
if height_count > 0:
    average_height = height_total / height_count
print (average_height)

