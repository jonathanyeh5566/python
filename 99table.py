# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:21:35 2020

@author: User
"""

evens=(i for i in range(1,21) if i%2==0) 
x=tuple(evens)
print(x)
print()

table99=((i,j,i*j) for i in range(1,10) for j in range(1,10))
x=tuple(table99)
print(x)
print()

for i in range(1,10):
    for j in range(1,10):
        table99=((i,j,i*j))
        x=tuple(table99)
        print(x,end=",")
    print()