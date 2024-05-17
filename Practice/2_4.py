from math import sqrt
from scipy import constants as scp

x_light = float(input("Enter the distance in light years: "))
v_frac = float(input("Input the speed as a fraction of the speed of light: "))

v = v_frac*scp.c
x = x_light*scp.light_year
gamma = 1/sqrt(1 - (v**2)/(scp.c**2))

t_rest = x/v
t_ship =gamma*(t_rest - (v*x)/(scp.c**2))

print("The time in the rest frame of an observer on Earth: ", t_rest)
print("The time as perceived by a passenger on board the ship: ",t_ship) 