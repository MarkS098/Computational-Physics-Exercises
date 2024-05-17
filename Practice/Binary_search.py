import matplotlib as mpl
import numpy as np
from scipy import constants as cnst

pi = cnst.pi
h = cnst.Planck
c = cnst.c
k_b = cnst.Boltzmann

def f(x):
    return 5*np.exp(-x) + x - 5
 
def binary(x_1,x_2,epsilon):
    
    if np.sign(f(x_1)) != np.sign(f(x_2)):
        x_tag = 0.5*(x_1 + x_2)
        val  = f(x_tag)
        
        if np.sign(f(x_tag)) == np.sign((f(x_1))):
            x_1 = x_tag
        else:
            x_2 = x_tag
        
        if np.abs(x_1 - x_2) > epsilon:
            x_tag = binary(x_1,x_2,epsilon)
        else:
            x_tag = 0.5*(x_1 + x_2)
    
    return x_tag
 
    
x_1 = 4.0
x_2 = 6.0
epsilon = 10**-6

x_tag = binary(x_1,x_2,epsilon)
print(x_tag)
x = np.linspace(0,10,1000)
mpl.pyplot.plot(x,f(x))
mpl.pyplot.grid(1)
