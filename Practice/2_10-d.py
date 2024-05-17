import scipy as scp
from math import *
from numpy import array

a = array([15.8, 18.3, 0.714, 23.2],float)

B_max = 0
Z_stab = 0

for Z in range(1,100):
    B_per = 0
    A_stab = 0
    for A in range(Z,3*Z):
        if A%2 != 0:
            a_5 = 0
        elif A%2 == Z%2 == 0:
            a_5 = 12.0
        elif A%2 == 0 & Z%2 != 0:
            a_5 = -12.0
    
        B = a[0]*A - a[1]*(A**(2/3)) - a[2]*((Z**2)/(A**(1/3))) - a[3]*(((A - 2*Z)**2)/A) + a_5/sqrt(A)
        B_per_temp = B/A
        
        if B_per < B_per_temp:
            B_per = B_per_temp
            A_stab = A
        
    print("The most stable value of A is:", A_stab," for the following Z value: ", Z)
    
    if B_max < B_per:
        B_max = B_per
        Z_max = Z
        
print("The value of the most stable binding energy per nucleon is:", B_max,"MeV")
print("The Z value for the maximum binding energy is: ", Z_max)