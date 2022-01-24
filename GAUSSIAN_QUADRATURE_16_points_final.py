# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 11:42:08 2022

@author: Sagnik Majumder
"""

# Gaussian Quadrature method numerical integration
print('16 point Gaussian Quadrature method numerical integration  : n = 16')
print('-------------------------------------------------------------------')

#importing modules
import numpy as np
from scipy.integrate import quad  

f = lambda x : np.exp(x)                        # Defyning integrand function
b = float(input('Enter upper limit of integration \n'))       # upper limit
a = float(input('Enter lower limit of integration \n'))       # lower limit


def qudra(f,a,b):                     # Defyning working function for GQ
    h = (b-a)/2
    m = (a+b)/2
    # Weights
    w = np.array([0.1894506104550685,0.1894506104550685,0.1826034150449236,
                  0.1826034150449236,0.1691565193950025,0.1691565193950025,
                  0.1495959888165767,0.1495959888165767,0.1246289712555339,
                  0.1246289712555339,
                  0.0951585116824928,0.0951585116824928,0.0622535239386479,
                  0.0622535239386479,0.0271524594117541,0.0271524594117541])
    # Abscissa for the interval [-1,+1]  :
    a = np.array([-0.0950125098376374,0.0950125098376374,-0.2816035507792589,
                  0.2816035507792589,-0.4580167776572274,0.4580167776572274,
                  -0.6178762444026438,0.6178762444026438,-0.7554044083550030,
                  0.7554044083550030,-0.8656312023878318,0.8656312023878318,
                  -0.9445750230732326,0.9445750230732326,-0.9894009349916499,
                  0.9894009349916499])
    
    # Value of integral by Legendre Gauss Quadrature Rule : h * sum on i from 0 to n [w[i]*f(h*a[i]+m)]
    
    integ = sum([w[i]*f(h*a[i]+m) for i in range (0,16)])
    integ = integ*h
    return integ

print('Integration by algorithm ' , qudra(f,a,b))
p = quad(f,a,b)
print('Integration by quad module ' , p)





















