# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:47:50 2022

@author: Sagnik Majumder
"""

'''
The Planck's energy distribution law
'''
print('Planck\'s energy distribution')
print('-----------------------------')

import math as m
import numpy as np
from matplotlib import pyplot

h = 6.626 * 10**(-34)      # PLANCK'S CONSTANT
c = 3 * 10**(8)            # SPEED OF LIGHT
k = 1.38 * 10**(-23)       # BOLTZMAN CONSTANT
u1 = h/(k*500)
u2 = h/(k*800)
u3 = h/(k*1000)
u4 = h/(k*1500)
u5 = h/(k*2500)
u6 = h/(k*3000)
u7 = h/(k*4000)


E1 = lambda n : ((8*m.pi*h*n**3)/c**3)*(1/(np.exp(u1*n)-1))
E2 = lambda n : ((8*m.pi*h*n**3)/c**3)*(1/(np.exp(u2*n)-1))
E3 = lambda n : ((8*m.pi*h*n**3)/c**3)*(1/(np.exp(u3*n)-1))
E4 = lambda n : ((8*m.pi*h*n**3)/c**3)*(1/(np.exp(u4*n)-1))
E5 = lambda n : ((8*m.pi*h*n**3)/c**3)*(1/(np.exp(u5*n)-1))
E6 = lambda n : ((8*m.pi*h*n**3)/c**3)*(1/(np.exp(u6*n)-1))
E7 = lambda n : ((8*m.pi*h*n**3)/c**3)*(1/(np.exp(u7*n)-1))
n = np.linspace(1,10**15,1000)
p1 = E1(n)
p2 = E2(n)
p3 = E3(n)
p4 = E4(n)
p5 = E5(n)
p6 = E6(n)
p7 = E7(n)

pyplot.plot(n,p1)
pyplot.plot(n,p2)
pyplot.plot(n,p3)
pyplot.plot(n,p4)
pyplot.plot(n,p5)
pyplot.plot(n,p6)
pyplot.plot(n,p7)
pyplot.show()
