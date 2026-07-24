from numpy import *

#values for b and c option
a = 0.001
b = 1000
c = 0.001

#a
def quadratic(a,b,c):
    a = eval(input("Enter a number to a:"))
    b = eval(input("Enter a number to b:"))
    c = eval(input("Enter a number to c:"))

    x1 = -b+sqrt(b**2-4*a*c)
    x2 = -b-sqrt(b**2-4*a*c)
    print("x1 =",x1)
    print("x2 =",x2)

#b
def quadratic_another(a,b,c):
    x1 = 2*c/-b+sqrt(b**2-4*a*c)
    x2 = 2*c/-b-sqrt(b**2-4*a*c)
    print("x1 =",x1)
    print("x2 =",x2)

#c
def quadratic_accurate(a,b,c):
    delta = sqrt(b**2-4*a*c)
    if b>=0:
        safe_term= -b-delta
    else:
        safe_term= -b+delta
    x1 = safe_term/(2*a)
    x2 = (2*c)/safe_term
    print("x1 =",x1)
    print("x2 =",x2)






