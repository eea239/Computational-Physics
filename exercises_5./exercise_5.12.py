import numpy as np

# constants
h_bar = 1.05e-34
K_B = 1.38e10-23
c = 3e8
p = (K_B**4)/(4*np.pi**2 * c**2 * h_bar**3)

def W(z,T):
    x_val = z / (1-z)
    return p * T**4 * ((x_val**3) / (np.exp(x_val)-1)) / ((1-z)**2)


# integral
def integral(T):
    a = 0.0
    b = 1.0
    N = 50
    x_standard , w_standard = np.polynomial.legendre.leggauss(N)
    # mapping
    xp = 0.5 * (b-a) * x_standard + 0.5 * (b+a)
    wp = 0.5 * (b-a) * w_standard

    integral_result = sum(wp*W(xp,T))
    return integral_result
T = 100
print(integral(T))

     
