import numpy as np
import pylab as plt


# constants
L = 10
G = 6.674e-11
M = 10000
A = L**2
sigma = M/A

def integrand(x,y,z):
    return 1/(x**2+y**2+z**2)**3/2

def Fz(z):
    a = -5
    b = 5
    N = 100
    x_standard, w_standard = np.polynomial.legendre.leggauss(N)

    # mapping
    xp = 0.5 * (b-a) * x_standard + 0.5 * (b+a)
    wp = 0.5 * (b-a) * w_standard
    integral_result = 0

    # double integral nested loops
    for i in range(N):
        for j in range(N):
            integral_result += wp[i] * wp[j] * integrand(xp[i],xp[j],z)
    
    return G * sigma * z * integral_result

# graphic
z_values = np.linspace(0,10,100)
F_values = []

for z in z_values:
    F_values.append(Fz(z))

plt.plot(z_values,F_values)
plt.xlabel("z distance(m)")
plt.ylabel("Gravity force at Z-axis")
plt.title("Gravitational Force")
plt.show()