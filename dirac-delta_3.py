'''
Creator - Sagnik Majumder
15-02-2022
DIRAC DELTA FUNCTION 3
'''


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci
def func(x,n):             # this will be the form of the dirac delta funcion
    return np.sin(n*(x-a0))/((np.pi)*(x-a0))
def f(x):                  # this will be the form of the function f(x)
    return (3*x-1)
for n in range (0,9):
    a0 = 5
    def h(x):
         return func(x,n)*f(x)
    print('Value of the given integration for n = ',n,'' , sci.quad(h,0.00001,a0+100))
    # plotting :
    x = np.linspace(-a0-10,a0+10,1000)
    plt.plot(x,func(x,n),label = n)
    plt.xlim(0,10)
    plt.xlabel('x')
    plt.ylabel('h(x)')
    plt.title('ploting property function multiplied with dirac delta fnc')
    plt.legend(prop = {'size':8})
    plt.grid()
    
'''
RESULT:
Value of the given integration for n =  0  (0.0, 0.0)
Value of the given integration for n =  1  (13.316246439388514, 1.5362507785823624e-07)
Value of the given integration for n =  2  (13.74615805977758, 1.5924358246211972e-07)
Value of the given integration for n =  3  (13.976817587644925, 3.991827703902062e-11)
Value of the given integration for n =  4  (14.128193087004707, 1.5446408414066124e-07)
Value of the given integration for n =  5  (14.190798734167323, 1.3291355558437631e-05)
Value of the given integration for n =  6  (14.172965509438052, 0.0018199657160823818)
Value of the given integration for n =  7  (14.112951431760928, 0.09314523283230425)
Value of the given integration for n =  8  (14.048514654452772, 2.5782875398374125)

WHICH IS CONSITANT WITH THE THEORITICAL RESULT.
'''