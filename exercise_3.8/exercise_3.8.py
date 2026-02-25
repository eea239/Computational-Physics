from pylab import *
from numpy import *


data = loadtxt("millikan.txt", float)

x_values = (data[:,0]) # all line, 0.column(Frequency)
y_values = (data[:,1]) # all line, 1.column (Voltage)

N = len(x_values)

# statistical calculations
Ex = mean(x_values)
Ey = mean(y_values)
Exx = mean(x_values**2)
Exy = mean((x_values)*(y_values))

# calculation of m and c
m = (Exy-Ex*Ey)/(Exx-Ex**2)
c = (Exx*Ey-Ex*Exy)/(Exx-Ex**2)
print("Calculated slope is",m)
print("Calculated intercept is",c)

# creating Leats-squares
y_fit = m*x_values + c


# writing graphics
scatter(x=x_values, y=y_values,color='blue')
plot(x_values,y_fit,color='red')
xlabel("Frequency (Hz)")
ylabel("Voltage (V)")
show()

# physical calculations
e = 1.602e-19
h = m*e
print("calculated new h is",h)

# comparison
hreal=6.626e-19
error = abs(h-hreal/h)*100
print("error percentage is",error)





