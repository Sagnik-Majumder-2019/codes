# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 17:04:51 2022

@author: sagnik
"""
"""
Thi code shows us that how to summation without any hesitation 
by the list comprehension method . We can easily sum without using
any loop directly and hence without any hesitation. Here I have done
the EXPONENTIAL FUNCTION , SINE FUNCTION AND COSINE FUNCTION
summation for this example.
"""
# Defyning the factorial function
def f(n):
   fac = n
   if n > 0 :
      for i in range (1,(n-1)):
         fac = fac*(n-i)
   elif n == 0 :
       fac = 1
   else :
       print('The factorial of a negative number doe\'s not exists')
   return fac

import math as m
# The summation by series comprehenion

# EXPONENTIAL SUMMATION
x = float(input('Enter value of number  : \n'))
j = int(input('Enter times of iteration : \n'))

ex = sum([x**(i)/f(i) for i in range (0,j)]) 
print('The value of the exponential is = ' , ex) 

# COSINE SUMMATION
theta = float(input('Enter value of angle in degree for cosine = \n'))
k = int(input("Enter number of iteration = \n"))
r = theta * (m.pi/180)
cos = sum([((-1)**(i))*(r**(2*i))/f(2*i) for i in range (0,k)])
print('The value of cosine(',theta,') is = ' , cos)

# SINE SUMMATION
theta1 = float(input('Enter value of angle in degree for sine = \n'))
k1 = int(input("Enter number of iteration = \n"))
r1 = theta1 * (m.pi/180)
sin = sum([((((-1)**(i))*(r1**(2*i+1)))/f(2*i+1)) for i in range (0,k1)])
print('The value of sine(',theta1,') is = ' , sin)

















