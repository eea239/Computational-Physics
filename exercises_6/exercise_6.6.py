import numpy as np
import scipy as sc
import vpython as vp

# parameters
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2 * k - m * omega * omega

# A matrix
A = np.empty([3,N],float)
A[0,:] = -k # 0.line: Upper diagonal values
A[1,:] = alpha # 1.line: Main diagonal values
A[2,:] = -k # 2.line: Lower diagonal values

# Boundary conditions (first and last elements of the main diagonal):
A[1,0] = alpha - k
A[1,N-1] = alpha - k

# v vector
v = np.zeros(N,float)
v[0] = C

# solution
solution = sc.linalg.solve_banded((1,1),A,v)

# ANIMATION

# shape
N = 26
spheres = []
vp.canvas(center=vp.vector(25, 0, 0), range=30)
for i in range(N):
    sphere = vp.sphere(pos=vp.vector(2*i,0,0),radius = 0.5, color=vp.color.red)
    spheres.append(sphere)

# moving
t = 0
dt = 0.05

while True:
    vp.rate(30)

    t = t + dt

    for i in range(N):
        displacement = np.real(2*solution[i] * np.exp(1j*omega*t))

        spheres[i].pos.x= 2 * i * displacement
