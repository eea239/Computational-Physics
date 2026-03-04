from numpy import exp,arange
from pylab import plot,show

def f(t):
    return exp(-t**2)

N = 1000
a = 0.0
E = []

T = arange(0.1,3,0.1)
for x in T:
    h = (x-a)/N

    s = f(a)+f(x)
    for k in range(1,int(N/2)+1):
        s += 4*f(a+(2*k-1)*h)
    for k in range(1,int(N/2)):
        s += 2*f(a+2*k*h)
        h*s/3
    E.append(float(h*s/3))
print(E)
plot(T,E)
show()
