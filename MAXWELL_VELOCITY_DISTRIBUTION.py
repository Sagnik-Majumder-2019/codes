# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 00:18:13 2022

@author: sagni
"""

from math import *
import numpy as num
import matplotlib.pyplot as plt
a = (5.31*10**(-26))/(2*pi*(1.38*10**(-23))*300)
b = (5.31*10**(-26))/(2*pi*(1.38*10**(-23))*500)
c = (5.31*10**(-26))/(2*pi*(1.38*10**(-23))*800)
d = (5.31*10**(-26))/(2*pi*(1.38*10**(-23))*1500)
print(a)
print(b)
print(c)
print(d)
maxwell = lambda v: 4*pi*100000*(a)**(3/2)*(v**2)*num.exp(-(a*pi)*v**2)
maxwell1 = lambda v: 4*pi*100000*(b)**(3/2)*(v**2)*num.exp(-(b*pi)*v**2)
maxwell2 = lambda v: 4*pi*100000*(c)**(3/2)*(v**2)*num.exp(-(c*pi)*v**2)
maxwell3 = lambda v: 4*pi*100000*(d)**(3/2)*(v**2)*num.exp(-(d*pi)*v**2)
v = num.linspace(0,200000,200000)
V = maxwell(v)
V1 = maxwell1(v)
V2 = maxwell2(v)
V3 = maxwell3(v)
plt.plot(v,V , color = 'r' , label = 'T = 300 K')
plt.plot(v,V1 , color = 'g' , label = 'T = 500 K')
plt.plot(v,V2 , color = 'y' , label = 'T = 800 K')
plt.plot(v,V3 , color = 'b' , label = 'T = 1500 K') 
plt.legend()
plt.grid()
plt.ylim(0,220)
plt.xlim(0,2650)
plt.xlabel('Velocity')
plt.ylabel('Num. of molecules')
plt.title('MAXWELLIAN VELOCITY DISTRIBUTION')
plt.show()



