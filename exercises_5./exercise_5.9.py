from numpy import *
from pylab import *

# constants
rho = 6.022e28 # number density of atoms
debye_temperature = 428 # debye temperature
V = 10e-3 # Volume
Kb = 1.38e-23 # boltzmann's constant
N = 50 # point number of Gaussian quadrature

# function
def f(x):
    return (x**4 * exp(x))/(exp(x)-1)**2

# integral
def cv(T):
    a = 0.0
    b = debye_temperature/T
    x_standard, w_standard = polynomial.legendre.leggauss(N)

    # mapping
    xp = 0.5 * (b-a) * x_standard + 0.5 * (b+a)
    wp = 0.5 * (b-a) * w_standard

    integral_result = sum(wp*f(xp))

    coefficient = 9*V*rho*Kb*(T/debye_temperature)**3
    return integral_result * coefficient

# graphics
T_value = linspace(5,500,100)
cv_value = [cv(T) for T in T_value]

figure(figsize=(8,5))
plot(T_value,cv_value,color='b',linewidth=2)
title('Heat Capacity of Aluminum (Debye Model)')
xlabel('Temperature (K)')
ylabel('Heat Capacity (J/K)')
grid(True)
show()
