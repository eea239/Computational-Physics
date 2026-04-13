from numpy import *
from pylab import *

def function(x):
    return x**4 -2*x +1
Ils =[]
for N in [10,20]:
    a = 0.0
    b = 2.0
    h = (b-a)/N
    s = 0.5*function(a) + 0.5*function(b)
    for k in range(1,N):
        s += function(a+k*h)

    Ils.append(h*s)

print('e2 =',(Ils[1]-Ils[0])/3)
print('fractional error =',(4.4-Ils[1])/4.4)


