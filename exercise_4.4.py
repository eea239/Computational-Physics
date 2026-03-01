from math import sqrt
N = 100
h = 2/N
I = 0
for k in range(1,N+1):
    xk = h*k -1
    yk = sqrt(1-xk**2)
    I += h*yk

print('I=',I)

