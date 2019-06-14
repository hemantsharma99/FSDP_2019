# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:10:03 2019

@author: admin
"""

user=input(">")
l1=user.split(" ")
l2=[ int(item) > 0 for item in l1]
l3=[item[::-1]==item for item in l1]
if all(l2) is True:
    print(any(l3))
else:
    print(all(l2))
