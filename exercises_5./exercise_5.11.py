from pylab import *
from numpy import *

# constants
lambda0 = 1
z = 3
N = 50
x_axis = linspace(-5,5,500)

# gauss
x_standard, w_standard = polynomial.legendre.leggauss(N)

# list
ratio_list = []

# function
def calculate_diffraction(x):
    u = x * sqrt(2/(lambda0*z))

    # integral limits
    a = 0.0
    b = u

    # mapping
    xp = 0.5 * (b - a) * x_standard + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w_standard

    # calculating integrals
    C = sum(wp*cos(0.5*pi*xp**2))
    S = sum(wp*sin(0.5*pi*xp**2))

    # ratio
    ratio = 1/8 *((2*C+1)**2+(2*S+1)**2)
    return ratio

# loop
for x in x_axis:
    ratio_list.append(calculate_diffraction(x))


# graphic

plot(x_axis, ratio_list,color='Blue',linewidth=2)
title('Near-field Diffraction')
xlabel('x(m)')
ylabel('I/I0')
grid(True)
show()