import numpy as np
import matplotlib.pyplot as plt
from scipy import log

x=np.linspace(-7.,9.,20)
y= 2.*x*x*x - 5*x*x - 50.*x +3.

fig = plt.figure()
plt.plot(x,y,linewidth=6.0) 
plt.show()

l = log(5.)
print (l)
