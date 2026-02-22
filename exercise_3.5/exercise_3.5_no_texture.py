from vpython import sphere,rate,vector,color
from numpy import pi,sin,cos,arange


#colors
yellow = (1,1,0)
white = (1,1,1)
orange = (1,0.6,0)
blue = (0,0,1)
gray = (0.5,0.5,0.5)
red = (1,0,0)
purple = (0.5,0,1)

sun = sphere(pos=vector(0,0,0),radius=0.5, color=vector(1,1,0))

#planets
jupiter = sphere(pos=vector(5,0,0),radius=0.45,color=vector(1,1,1))
saturn = sphere(pos=vector(6,0,0),radius=0.42,color=vector(1,0.6,0))
earth = sphere(pos=vector(3,0,0),radius=0.4,color=vector(0,0,1))
venus = sphere(pos=vector(2,0,0),radius=0.38,color=vector(0.5,0.5,0.5))
mars = sphere(pos=vector(4,0,0),radius=0.35,color=vector(1,0,0))
mercury = sphere(pos=vector(1,0,0),radius=0.32,color=vector(0.5,0,1))

#moving
theta=0
dt=0.05

while True:
    rate(30)

    theta = theta + dt

    jupiter.pos=vector(7*cos(theta*0.08),7*sin(theta*0.08),0)
    saturn.pos=vector(9*cos(theta*0.03),9*sin(theta*0.03),0)
    earth.pos=vector(3.5*cos(theta),3.5*sin(theta),0)
    venus.pos=vector(2.5*cos(theta*1.6),2.5*sin(theta*1.6),0)
    mars.pos=vector(5*cos(theta*0.5),5*sin(theta*0.5),0)
    mercury.pos=vector(1.5*cos(theta*4.1),1.5*sin(theta*4.1),0)