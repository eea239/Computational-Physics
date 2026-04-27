
# a
from numpy import *

def f(x):
  return (sin(sqrt(100*x))**2)

N = 1
a = 0.0
b = 1.0
h = (b-a)/N
s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
  s += f(a+k*h)

I_old = s*h
e = 6.02e23
N = 2
while abs(e) > 1e-6:
  h = (b-a)/N
  I = I_old
  for k in range(1,N):
    if k%2 != 0:

      I += h*f(a+k*h)
  e = (I-I_old)/3
  print('I=',I,';error=',e,'; N=',N)
  N*=2
  I_old = I


  # b

  def f(x):
      return (sin(sqrt(100 * x)) ** 2)


  N = 1
  a = 0.0
  b = 1.0
  size = 10
  R = zeros([size,size],dtype=float)
  e = 6.02e23
  i = 0
  while abs(e) > 1e-6:
    h = (b-a)/N

    s = 0.5*f(a)+0.5*f(b)
    for k in range(1,N):
        s += f(a+k*h)

    R[i,0] = h*s
    for m in range(1,i+1):
        R[i,m]= R[i,m-1] + (R[i,m-1] - R[i-1,m-1])/(4**m-1)
        e = (R[i,m-1] - R[i-1,m-1])/(4**m-1)

    N *= 2
    i += 1
for i in range(size):
    if R[i,0] != 0.0:
        print(*round(R[i,:],6)[R[i,:] !=0])
