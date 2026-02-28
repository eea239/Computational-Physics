from numpy import *
def f(x):
    return x*(x-1)

def derivates():
    for sigma in [1e-2,1e-4,1e-6,1e-8,1e-10,1e-12,1e-14]:
        x=1
        df = (f(x+sigma)-f(x))/sigma
        print('sigma=',sigma,'df/dx:',df)

derivates()