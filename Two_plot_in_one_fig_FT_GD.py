# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 21:14:32 2022

@author: sagnik
"""

# Fourier transform oof Gaussian function
# Importing necessary modules
import math as m 
import numpy as np
import matplotlib.pyplot as plt

# Defyning Variables
f= lambda x:(3)*np.exp(-2*x**2)
F= lambda k:(3/2)*np.exp(-(k**2)/4*2)
x = np.linspace(-10,10,100)
k = np.linspace(-10,10,100)
X = f(x)
K = F(k)

# Defyning Subplots
plot1=plt.subplot2grid((3,3),(0,0),colspan=2)
plot2=plt.subplot2grid((3,3),(2,0),colspan=2)

# Plotting first Subplot
plot1.plot(k,K, color='r',alpha=1.0)
plot1.set_title('k-space')
plot1.set_xlabel('k')
plot1.set_ylabel('F(k)')
plot1.text(-10.5,2.5,'Fourier transform of Gaussian function')                       # Adding text in figure
plot1.grid()

# Plotting second Subplot
plot2.plot(x,X, color = 'violet',alpha=1.0)
plot2.set_title('x-space')
plot2.set_xlabel('x')
plot2.set_ylabel('f(x)')
plot2.text(-6.5,4.5,'Given Gaussian function')                                       # Adding text in figure
plot2.grid()

plt.show()