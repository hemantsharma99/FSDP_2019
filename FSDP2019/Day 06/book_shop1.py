# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:51:56 2019

@author: admin
"""
t1=[]
orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
for item in orders:
    y=item[-1]*item[-2]
    if y<100:
        l1=(item[0],y+10)
        t1.append(l1)
    else:
        l1=(item[0],y)
        t1.append(l1)
print(t1)




orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
order=map(lambda x:(x[-1]*x[-2])+10 if x[-1]*x[-2]<100 else x[-1]*x[-2],orders)
order1=map(lambda x:x[0],orders)
zipped=zip(order1,order)
l1=list(zipped)