from pylab import plot,scatter,show,imshow
from numpy import *

N = 400
img_matrix=zeros((N,N))

x_values=linspace(-2,2,N)
y_values=linspace(-2,2,N)
for i in range(N):
    for j in range(N):

        x= x_values[j]
        y= y_values[i]

        c = complex(x,y)
        z = 0

        for k in range(100):
            z = z**2 + c
            if abs(z)>2:
                img_matrix[i,j]=1
                break

imshow(img_matrix,cmap='gray')
show()


