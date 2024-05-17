import numpy as np
import matplotlib as mpl

N = 5000
nbins = 100
A = np.random.randn(N,N)
upper_A = np.triu(A)
lower_A = np.transpose(upper_A)

A_herm = upper_A + lower_A
np.fill_diagonal(A_herm, 0)

x,V = np.linalg.eigh(A)
print("The hermitian matrix is: ", A_herm)
print("The eigenvalue vector is: ",x)

mpl.pyplot.hist(x,nbins,density=True)