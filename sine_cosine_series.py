# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 09:01:26 2022

@author: sagnik
"""

import math as m

def fact(n):               # defining the factorial
    fac = 1
    for i in range (0,(n-1)):
        fac = fac * (n-i)
    return fac

# cosine series 


x = eval(input('Enter value of angle in degree : \n' ))
t = x*((m.pi)/180)         #convert to radians
summ = 1
n = 1
term = 1
for i in range (1,50):
    Term = ((-1)**i)*(t**(2*i)/fact(2*i))
    summ  = summ + Term
print('The calculated value of cosine is', summ) 
print('The actual value of cosine is ' ,m.cos(t))

print('\n')
# sine series
print('\n')

y = eval(input('Enter value of angle in degree : \n'))
r = y*(m.pi)/180            # convert to radians
sum = r
for i in range (1,80):
    term1 = ((-1)**i)*(r**(2*i+1)/fact(2*i+1))
    sum += term1
print('The calculated value of sine is ' ,sum)
print('The actual value of sine is ' , m.sin(r))