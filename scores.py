# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
sc=((89,88,75),(10,58,94),(49,67,90))
aveg=((x+y+z)/3 for x,y,z in sc)
x=tuple(aveg)
print(x)

aveg1=(sum(i)/len(i) for i in sc)
y=tuple(aveg1)
print(y)

ar=(round(i,2)for i in y)
z=tuple(ar)
print(z)