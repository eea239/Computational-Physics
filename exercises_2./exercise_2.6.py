
from math import pi

l1 = float(input("Enter the distance of planet to the Sun: "))
v1 = float(input("Enter the velocity of planet at perihelion: "))
M = 1.98e30
G = 6.6738e-11
m = 5.972e24
v = 29.78
r = 149_597_871

E = 1/2*m*v**2 - G*m*M/r

v2 = ((v1**2 - 2*G*M/l1)* (-v1*l1/2*G*M))**(1/2)
l2 = l1*v1/v2

a = 1/2*(l1+l2)
b = (l1*l2)**1/2
T = 2*pi*a*b/l1*v1
e = l2-l1/l2+l1

print("Total Energy: E =",E)
print("Semi-major axis: a = ",a)
print("Semi-minor axis: b = ",b)
print("Orbital period: T = ",T)
print("Orbital eccentricity: e = ",e)