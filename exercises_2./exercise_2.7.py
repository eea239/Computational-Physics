C = 1
n = 0
print(C)
while C<= int(1e9):
    C = (4*n+2) * C/(n+2)
    n += 1
    print(C)