# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 12:21:54 2022

@author: sagni
"""

# INFINITE SERIES
# EXPONENTIAL SERIES
# e^x = 1+x+(x^2/2!)+(x^3/3!)+(x^4/4!)+...
import math
# without accurancy level
x = eval(input('Enter the value of x = '))
sum = 1
term = 1
for n in range (1,1000000):
    term = term*(x/n)
    sum += term
   
print(sum,math.exp(2))



y , t = eval(input('Enter values of y and t (accurancy level) = '))
val , ter = 0 , 1
n = 1
while ter > t :
    val = val + ter
    ter = ter * (y/n)
    n = n+1
print('Value by loop = ' , val  ,'Value by math pack = ' , math.exp(y))
