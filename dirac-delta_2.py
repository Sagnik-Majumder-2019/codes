'''
Creator - Sagnik Majumder
14-02-2022
DIRAC DELTA FUNCTION 2
'''


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci
def func(x,n):             # this will be the form of the dirac delta funcion
    return (n/np.pi)*(1/(1+(n**2*(x-a0)**2)))
def f(x):                  # this will be the form of the function f(x)
    return x
for n in range (0,8):
    a0 = 5
    def h(x):
         return func(x,n)*f(x)
    print('Value of the given integration for n = ',n,'' , sci.quad(h,a0-100,a0+100))
    x = np.linspace(-a0-3,a0+6,1000)
    plt.plot(x,func(x,n),label=n)
    plt.xlim(2,8)
    plt.xlabel('x')
    plt.ylabel('h(x)')
    plt.title('ploting property function multiplied with dirac delta fnc')
    plt.legend(prop = {'size':14})
    plt.grid()
    
    
'''
RESULT :
Value of the given integration for n =  0  (0.0, 0.0)
Value of the given integration for n =  1  (4.968170072350957, 5.4586312180579216e-08)
Value of the given integration for n =  2  (4.984084638317977, 2.341540479566043e-08)
Value of the given integration for n =  3  (4.989389709757794, 6.608113450632265e-09)
Value of the given integration for n =  4  (4.992042269424022, 1.6400067939719825e-08)
Value of the given integration for n =  5  (4.993633810764569, 7.023550049031275e-11)
Value of the given integration for n =  6  (4.994694840142451, 6.609892838815512e-09)
Value of the given integration for n =  7  (4.995452719005062, 6.850487937296212e-08)
'''



