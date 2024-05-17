from math import *
from numpy import *

M = 0.0
L = int(input("Enter the size of the lattice L/2: "))

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if i == j == k ==0:
                continue
            
            r = (sqrt(i**2 + j**2 + k**2))**-1
            
            if (i + j + k)%2 == 0:
                M+= r
            else:
                M-= r
print(M)