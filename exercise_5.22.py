import numpy as np
import math as math

N = 10000
k = np.arange(N)
z_k = np.exp(1j * 2 * np.pi * k / N)


# value of m
for m in range(1,21):
    m_factorial = math.factorial(m)

    # summation
    terms = np.exp(2 * z_k) * np.exp(-1j * 2 * np.pi * k * m / N)
    summation = np.sum(terms)

    # Result
    result = (m_factorial / N) * summation
    print(result)