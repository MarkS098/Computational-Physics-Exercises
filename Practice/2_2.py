from scipy import constants as scp

G = scp.gravitational_constant # (m^3)/(kg*s^2)
pi = scp.pi
M_earth = 5.97e24 # kg
R_earth = 6371000 # m

T = float(input("Enter the time for the altitude:"))

h = ((G*M_earth*(T)**2)/(4*pi**(2)))**(1/3) - R_earth

print("The altitude at the requested time is",h,"meters")
     