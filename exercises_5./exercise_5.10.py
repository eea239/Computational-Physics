from numpy import *
from pylab import *

# list
T_list = []

# function
def T(m,x,a):
    m = 1
    return sqrt(8*m) * 1/sqrt(a**4-x**4)

# integral
def integral(amplitude):
    N = 20
    b = amplitude
    a = 0
    x_standard, w_standard = polynomial.legendre.leggauss(N)

    # mapping
    xp = 0.5 *(b-a) * x_standard + 0.5 * (b+a)
    wp = 0.5 *(b-a) * w_standard

    integral_result = sum(wp*T(1,xp,amplitude))
    return integral_result

# loop to draw graphic
for i in linspace(0.01,2,100):
    calculated_period = integral(i)
    T_list.append(calculated_period)
    amplitudes = linspace(0.1,1,100)

# graphic
figure(figsize=(8,5))
title('Anharmonic Oscillator')
xlabel('Amplitude')
ylabel('Time/Period')
plot(amplitudes,T_list,color='red',linewidth=2)
show()