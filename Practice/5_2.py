'''
This program calculates an approximate integral of the function x^2 + 2x + 1 using
using Simpsons rule

N - number of slices
a - lower integral bound
b - upper integral bound
'''

# Function to integrate
def f(x):
    return x**4 - 2*x + 1

def simpson(a,b,N,I_known):
    h = (b - a)/N

    I = f(a) + f(b)

    # Summation over odd and even parts
    for k in range(1,N,2):
        I += 4*f(a + k*h)

    for k in range(2,N,2):
        I += 2*f(a + k*h)
    
    I *= (h/3)
    frac_err = ((I - I_known)/I_known)*100
    
    return I,frac_err


# Defining the integration constants 
N_arr = [10,100,1000]
a = 0.0 
b = 2.0 
I_known = 4.4

for j in range(0,3):
    N = N_arr[j]
    result = simpson(a,b,N,I_known)
    I, frac_err = result
    print("The value of the integral for", N," slices is:", I)
    print("The fractional error for ", N," slices is:", frac_err,"%\n")