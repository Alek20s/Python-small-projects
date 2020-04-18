import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(-np.pi,np.pi,100)

tri=0.5
kappa =2.

x= 0.75* np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y=0.75* kappa*np.sin(theta)

fig = plt.figure()
ax=fig.gca()
ax.set_aspect('equal')

plt.plot(x,y,linewidth=2.0)#,label= " CANDY Growth Rate", markersize =1 )

tri=0.5
kappa =1.
x= np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y1= kappa*np.sin(theta)
plt.plot(x,y1,linewidth=2.0)

tri=0.
kappa =1.0
x= np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y2=  kappa*np.sin(theta)
plt.plot(x,y2,linewidth=2.0)


plt.xlabel ('Minor Radius', fontsize = 20)
plt.ylabel ('Z', fontsize =20)

plt.xlim((-1.4, 1.4))

plt.ylim((-1.8, 1.8))
plt.title ('Geometry',fontsize = 22 )

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)  

plt.grid(True)
plt.legend()
plt.show()
