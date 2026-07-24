from vpython import sphere, rate, vector, color

L = 5
R = 0.1

#a
for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L + 1):

            if (i + j + k) % 2 == 0:
                atom_color = color.blue
            else:
                atom_color = color.cyan

            sphere(pos=vector(i, j, k), radius=R, color=atom_color)


#b
my_color = vector(1,0.84,0)
for i in range(-L, L):
    for j in range(-L, L):
        for k in range(-L, L):

            # corner atom
            sphere(pos=vector(i, j, k), radius=R, color=my_color)

            # surface centers
            sphere(pos=vector(i+0.5,j+0.5,k), radius=R, color=my_color)
            sphere(pos=vector(i+0.5,j,k+0.5), radius=R, color=my_color)
            sphere(pos=vector(i,j+0.5,k+0.5), radius=R, color=my_color)

while True:
    rate(30)





