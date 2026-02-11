
# constants
m = 9.11e-31
E = 10
V = 9
h_bar = 1.05e-31


k1 = (2*m*E/h_bar)**1/2
k2 = (2*m*(E-V)/h_bar)**1/2

T = 4*k1*k2/(k1+k2)**2
R = (k1-k2/k1+k2)**2

print("The transmission probability is",T)
print("The reflection probability is",R)