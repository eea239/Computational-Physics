def factorial(n):
    f = 1.0
    for k in range(1, n+1):
        f*=k

    return f
def binomial(n,k):
    if k==0:
        return 1
    else:
        return factorial(n)/(factorial(k)*factorial(n-k))

for n in range(1,21):
    ls=[]
    for k in range(n+1):
        ls.append(binomial(n,k))

    print(*ls,sep=" ")



