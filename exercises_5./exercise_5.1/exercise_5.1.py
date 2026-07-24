from numpy import loadtxt
from pylab import show,scatter,plot,xlabel,ylabel

data = loadtxt('velocities.txt', float)

t_values = data[:,0]
v_values = data[:,1]

N = len(t_values)
a = t_values[0]
b = t_values[-1]
h = (b-a)/N
s = 0.5*v_values[0] + 0.5*v_values[-1]
sls =[s]

for k in range(1,N):
    s += v_values[k]
    sls.append(s)
print(h*s)
plot(t_values,v_values)
plot(t_values,sls)

xlabel('time')
ylabel('velocity')

show()


