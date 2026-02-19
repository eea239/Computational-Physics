from pylab import *
from numpy import sin,cos,pi

#a

theta = linspace(0,2*pi,100)
x = 2*cos(theta) + cos(2*theta)
y = 2*sin(theta) - sin(2*theta)

plot(x,y)
show()

#b
theta = linspace(0,10*pi,100)
r = theta**2
x = r*sin(theta)
y = r*cos(theta)
plot(x,y)
show()

#c
theta = linspace(0,24*pi,10000)
r = exp(cos(theta)) - 2*cos(4*theta) + sin(theta/12)**5
x = r*sin(theta)
y = r*cos(theta)
plot(x,y)
show()


