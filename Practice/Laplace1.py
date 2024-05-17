import numpy as np
import pylab as pl

L = 1 # Meters
N = 100
V = 1
omega = 0.9
target = 1e-6
delta = 1


phi_arr = np.zeros([N+1,N+1], float)
phi_arr[0,:] = V

while delta > target:
    delta = 0
    for i in range(1,N):
        for j in range(1,N):
            phi_old = phi_arr[i,j]
            phi_arr[i,j] = ((1 + omega)/4)*(phi_arr[i + 1,j] + phi_arr[i - 1,j]\
                           + phi_arr[i,j + 1] + phi_arr[i,j - 1]) -omega*phi_arr[i,j] 
            epsilon = np.abs(phi_arr[i,j] - phi_old)
            
            if epsilon > delta:
                delta = epsilon

pl.imshow(phi_arr)
pl.gray()