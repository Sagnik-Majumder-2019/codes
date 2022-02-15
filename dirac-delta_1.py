'''
Creator - Sagnik Majumder
14-02-2022
DIRAC DELTA FUNCTION 1 
'''


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci
def func(x,n):             # this will be the form of the dirac delta funcion
    return (n/np.sqrt(np.pi))*np.exp(-n**2*(x-a0)**2)
def f(x):                  # this will be the form of the function f(x)
    return x**2
for n in range (0,8):
    a0 = 8
    def h(x):
         return func(x,n)*f(x)
    print('Value of the given integration for n = ',n,'' , sci.quad(h,a0-100,a0+100))
    x = np.linspace(-a0-3,a0+6,1000)
    plt.plot(x,func(x,n),label = n)
    plt.xlim(5,11)
    plt.xlabel('x')
    plt.ylabel('h(x)')
    plt.title('ploting property function multiplied with dirac delta fnc')
    plt.legend(prop = {'size':14})
    plt.grid()
    
    
'''
RESULT :
Value of the given integration for n =  0  (0.0, 0.0)
Value of the given integration for n =  1  (64.49999999999999, 5.8098673735050835e-09)
Value of the given integration for n =  2  (64.12500000000001, 6.794795835645486e-09)
Value of the given integration for n =  3  (64.05555555555554, 4.3131079352687066e-11)
Value of the given integration for n =  4  (64.03125, 7.052941715283308e-09)
Value of the given integration for n =  5  (64.02000000000001, 2.9047511058679906e-07)
Value of the given integration for n =  6  (64.01388888888891, 4.258499229658276e-11)
Value of the given integration for n =  7  (64.01020408163271, 7.416800381631725e-11)

'''



