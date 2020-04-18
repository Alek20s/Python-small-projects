import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(-np.pi,np.pi,100)

tri=0.0
kappa =2.

x=  np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y= kappa*np.sin(theta)

fig = plt.figure()
ax=fig.gca()
ax.set_aspect('equal')

plt.plot(x,y,linewidth=2.0)

tri=0.0
kappa =1.2
x= 0.6*np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y1= 0.6 * kappa*np.sin(theta)
plt.plot(x,y1,'b-',linewidth=2.0)

tri=0.0
kappa =1.0
x= 0.4*np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y1= 0.4 * kappa*np.sin(theta)
plt.plot(x,y1, 'b-',linewidth=2.0)



tri=0.
kappa =1.5
x= 0.8*np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y2= 0.8* kappa*np.sin(theta)
plt.plot(x,y2, 'b-',linewidth=2.0)


plt.xlabel ('Minor Radius', fontsize = 20)
plt.ylabel ('Z', fontsize =20)

plt.xlim((-1.4, 1.4))

plt.ylim((-2.1, 2.1))
plt.title ('Elongation Derivative',fontsize = 18 )

plt.xticks(fontsize=14)
plt.yticks(fontsize=18)  

plt.grid(True)
plt.legend()
plt.show()
