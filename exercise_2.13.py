def catalan(n):
    if n==0:
        return 1
    else:
        return int((4*n-2)*catalan(n-1))/n+1

print(catalan(100))

def g(m,n):
    if n==0:
        return m
    else:
        return g(n,m%n)

print(g(108,192))





