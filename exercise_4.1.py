def factorial_int(n):
    if n == 0:
        return 1
    else:
        return int(n * factorial_int(n-1))
print(factorial_int(200))

def factorial_float(n):
    n = float(n)
    if n == 0.0:
        return 1.0
    else:
        return float(n * factorial_float(n-1))
print(factorial_float(200))

# Python retrieved large value inf in float