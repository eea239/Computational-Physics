
def f(x):
    return x**4-2*x+1
for N in [10,100,1000]:

    a = 0.0
    b = 2.0
    h = (b-a)/N

    s = f(a)+f(b)
    for k in range(1,int(N/2)+1):
        s += 4*f(a+(2*k-1)*h)
    for k in range(1,int(N/2)):
        s += 2*f(a+2*k*h)

    print(h*s/3)

