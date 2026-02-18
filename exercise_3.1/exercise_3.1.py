from pylab import plot, show
from numpy import loadtxt

data = loadtxt('sunspots.txt')
Yls = []
for i in range(1000):
    Y = 0.0
    r = 5
    for m in range(-r, r+1):
        Y += data[i+m,1]/(2*r+1)

    Yls.append(Y)
x = data[:1000,0]
y = data[:1000,1]
plot(x,y)
show()







