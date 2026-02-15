import numpy as np


# constants
a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2

#a
A = float(input("Please enter the mass number:"))
Z = float(input("Please enter the atomic number:"))


if A % 2 == 0  and Z % 2 == 0:

    a5 = 12

elif A % 2 != 0:

    a5 = 0

else:
    a5 = -12

 B = a1*A - a2*(A**(2/3)) - a3*Z*(Z-1) /(A**(1/3)) - a4*(A-2*Z)**2/A + a5/(A**(1/2))

print(B)

#b
per_nucleon = B/A
print(per_nucleon)

#c
Z = int(input("Please enter the atomic number:"))
BperA = 0.0
BestA = Z
for A in np.linspace(Z, 3*Z, 2*Z+1):

    A = int(A)
    if Z % 2 == 0:
        a5 = 12

    elif Z % 2 != 0:
        a5 = 0

    else:
        a5 = -12

 B = a1*A - a2*(A**(2/3)) - a3*Z*(Z-1) /(A**(1/3)) - a4*(A-2*Z)**2/A + a5/(A**(1/2))

if B/A > BperA:
     BperA = B/A
     BestA = A

 print("Atomic number Z =",Z, "Mass number A = ", BestA, "Binding Energy per Nucleon B/A=",BperA)

#d
np.linspace(1, 100, 101)







