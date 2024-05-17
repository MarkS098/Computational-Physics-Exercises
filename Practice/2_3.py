
from math import sqrt, atan, pi
x = float(input("Enter x:"))
y = float(input("Enter y:"))

r = sqrt(x**2 + y**2)
theta = atan(y/x)*180/pi

print("r =", r,"theta =", theta)