from numpy import *
from pylab import *

def bessel_integrand(m,x,theta):
    return cos(m*theta-x*sin(theta))
def J(m,x):
    N = 1000
    a = 0.0
    b = pi
    h = (b-a)/N
    s = bessel_integrand(m,x,a) + bessel_integrand(m,x,b)
    for k in range(1,int(N/2)+1):
        s += 4*bessel_integrand(m,x,a+(2*k-1)*h)
    for k in range(1,int(N/2)):
        s += 2*bessel_integrand(m,x,a+2*k*h)
    return h*s/(3*pi)
def In(r):
    lamb=500e-9
    k = 2*pi/lamb
    return (J(1,k*r)/(k*r))**2
x = linspace(-1e-6,1e-6,100)
y = linspace(-1e-6,1e-6,100)
I = zeros([100,100],dtype=float)
for i in range(100):
    for j in range(100):
        r = sqrt(x[i]**2+y[j]**2)
        I[i,j]=In(r)
imshow(I,cmap='hot',vmax=0.01)
show()

