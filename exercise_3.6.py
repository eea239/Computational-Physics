from pylab import show,scatter,plot,imshow
from numpy import arange,full


for r in arange(1, 4, 0.01):
    x = 1/2
    xls=[]
    rls=[]
    for n in range(100):
        x = r*x*(1-x)

    for n in range(100):
        x = r*x*(1-x)
        xls.append(x)
        rls.append(r)
        plot(r,x,"ko")


show()












