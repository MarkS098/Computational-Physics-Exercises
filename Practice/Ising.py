import numpy as np
import matplotlib.plot as plt




def E(J,arr):
    return -J*np.sum((np.roll(arr,1,0)*arr + np.roll(arr,1,1)*arr))

runs = 10000
J = 1
N = 20
T = 2
spin_arr = np.random.randint(2, size = (N,N))
spin_arr[np.nonzero(spin_arr < 1)] = -1
M_arr = []
for k in range(runs):
    M_arr = np.append(M_arr, np.sum(spin_arr))
    E_old = E(J,spin_arr)
    i = np.random.randint(N)
    j = np.random.randint(N)
    spin_arr[i,j] = -spin_arr[i,j]
    E_new = E(J,spin_arr)
    
    dE = E_new - E_old
    
    if dE > 0:
        if np.random.rand(1) > np.exp(-dE/T):
            E_new = E_old
            spin_arr[i,j] = -spin_arr[i,j]

plt.plot(M_arr)
