import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
x1, y1 = np.loadtxt('real.txt', skiprows=1, unpack=True)

sx1=0
sy1=0
sxx1 =0
sxy1 =0
k=0
while k<13:
    sx1 = sx1+x1[k]
    sy1 = sy1+y1[k]
    sxx1 = sxx1 + x1[k]*x1[k]
    sxy1 = sxy1 +x1[k]*y1[k]
    k= k+1

b1= (-13*sxy1 + sx1*sy1)/(sx1*sx1-13*sxx1)
a1 =(sy1-b1*sx1)/13
print (a1, b1)  

x = np.arange(0, 15)
y = a1+b1*x

f = interpolate.interp1d(x, y)

plt.plot(x1, y1, 'o')
plt.plot(x, y)
plt.show()

x1, y1 = np.loadtxt('real.txt', skiprows=1, unpack=True, dtype=np.str)


