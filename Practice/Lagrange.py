from scipy import constants as cnst
import numpy as np

G = cnst.G
M = 5.9741e24
m = 7.3481e22
R = 3.844e8
omega = 2.662e-6


def f(r):
    return G*M/r**2 - G*m/(R - r)**2 - r*omega**2

r_1 = 0.01*R
r_2 = 0.99*R
f_2 = f(r_1)

epsilon = 1e-10

while np.abs(r_1 - r_2) > epsilon:
    f1,f2 = f(r_1),f(r_2)
    r_1,r_2 = r_2,r_2 - f(r_2)*((r_2 - r_1)/(f(r_2) - f(r_1)))

print("The orbits radius is: ",r_2/1000,"m")