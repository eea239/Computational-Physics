from vpython import *
from numpy import *

canvas(width=800, height=800)
sun = sphere(pos=vector(0,0,0),texture='sun.jpg',radius=695500/5e4)

mercury = sphere(pos=vector(57.900,0,0),texture='mercury.jpg',radius=2440/1000)
venus = sphere(pos=vector(108.20,0,0),texture='venus.jpg',radius=6052/1000)
earth = sphere(pos=vector(149.60,0,0),texture='earth.jpg',radius=6371/1000)
mars = sphere(pos=vector(227.90,0,0),texture='mars.jpg',radius=3386/1000)
jupiter = sphere(pos=vector(778.50,0,0),texture='jupiter.jpg',radius=69173/1000)
saturn = sphere(pos=vector(1433.4,0,0),texture='saturn.jpg',radius= 57316/1000)
for theta in arange(0,10000000,0.1):
    rate(300)
    mercury.pos = vector(57.900*cos(theta/88.0000),57.900*sin(theta/88.0000),0)
    venus.pos = vector(108.20*cos(theta/224.700),108.20*sin(theta/224.700),0)
    earth.pos = vector(149.60*cos(theta/365.300),149.60*sin(theta/365.300),0)
    mars.pos = vector(227.90*cos(theta/587.000),227.90*sin(theta/587.000),0)
    jupiter.pos = vector(778.70*cos(theta/4331.60),778.70*sin(theta/4331.60),0)
    saturn.pos = vector(1433.4*cos(theta/10759.2),1433.4*sin(theta/10759.2),0)

while True:
    rate(100)