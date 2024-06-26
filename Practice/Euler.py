from math import sin
import numpy as np
import matplotlib as mpl

def f(x,t):
    return -x**3 + sin(t)

x1 = 0.0
x2 = 10.0
N = 1000
h = (x2 - x1)/N
x_init = 0.0

t_arr = np.arange(x1,x2,h)
x_arr = np.zeros(len(t_arr))

for t in range(2,len(t_arr)):
    x_arr[t] = x_arr[t-1] + h*f(x_arr[t-1],t_arr[t])
    
mpl.pyplot.plot(t_arr,x_arr)