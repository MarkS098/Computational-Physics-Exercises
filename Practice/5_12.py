from scipy import constants as cnst
from numpy import exp


def f(z):
    return (1/((1-z)**2))*((z/(1-z))**3)/(exp(z/(1-z)) - 1)

def simpson(a,b,N):
    h = (b - a)/N

    I = f(a) + f(b)

    # Summation over odd and even parts
    for k in range(1,N,2):
        I += 4*f(a + k*h)

    for k in range(2,N,2):
        I += 2*f(a + k*h)
    
    I *= (h/3)
    
    return I

# Constants
c = cnst.c
h_bar = cnst.hbar
k_b = cnst.k
pi = cnst.pi
sigma = cnst.sigma

A = ((k_b)**4)/(4*(pi**2)*(c**2)*(h_bar**3))


a = 0.01 
b = 0.99
N = 1000

I = simpson(a,b,N)
I_tot = A*I
sigma_est = I_tot/sigma

print("The value of the integral is: ",I)
print("The estimate for sigma is: ",sigma_est)