from math import tanh
from numpy import arange, zeros, cosh
from matplotlib import pyplot as plt

def f(x):
    return 1 + (1/2)*(tanh(2*x))

def deriv(x,h):
    return (f(x + h) - f(x - h))/(2*h)

low_bound = -2
high_bound = 2
h = 0.001 

x_arr = arange(low_bound, high_bound,h)
deriv_arr = zeros((len(x_arr)))

for i in range(0,len(x_arr)):
    deriv_arr[i] = deriv(x_arr[i],h)
    
plt.plot(x_arr,deriv_arr,'o')
plt.plot(x_arr,1/((cosh(2*x_arr))**2))