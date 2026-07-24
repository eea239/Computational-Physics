import numpy as np
import pylab as plt

def f(x):
    return 1 + 1/2*(np.tanh(2*x))

def central_difference(f,x,h=1e-5):
    return (f(x+h)-f(x-h)) / (2*h)

x_values = np.linspace(-2,2,100)

derivate_values =[]

for x in x_values:
    derivate_values.append(central_difference(f,x))

def sech2(x_values):
    return 1 / (np.cosh(2*x_values)**2)

# graphic
plt.plot(x_values,derivate_values,label='numerical derivative')
plt.plot(x_values,sech2(x_values),'--',label='real derivate')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('derivate of 1+1/2tanh(2x)')
plt.legend()
plt.grid(True)
plt.show()
