from numpy import loadtxt
from pylab import scatter, imshow, show,gray,jet

data = loadtxt('stm.txt', float)
imshow(data, origin='lower')
jet()
show()

