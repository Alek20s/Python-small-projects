import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(-np.pi,np.pi,100)

tri=0.8
kappa =1.2

x=  np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y= kappa*np.sin(theta)

fig = plt.figure()
ax=fig.gca()
ax.set_aspect('equal')

plt.plot(x,y, c='g',linewidth=2.0)#,label= " CANDY Growth Rate", markersize =1 )

# , c='b', label='y1',linewidth=7.0)

tri=0.25
kappa =1.2
x= 0.6*np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y1= 0.6 * kappa*np.sin(theta)
plt.plot(x,y1,'g-',linewidth=2.0)

tri=0.0
kappa =1.1
x= 0.4*np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y1= 0.4 * kappa*np.sin(theta)
plt.plot(x,y1, 'g-',linewidth=2.0)



tri=0.6
kappa =1.2
x= 0.8*np.cos(theta + (np.arcsin(tri))*(np.sin(theta)))
y2= 0.8* kappa*np.sin(theta)
plt.plot(x,y2, 'g-',linewidth=2.0)


plt.xlabel ('Minor Radius', fontsize = 22)
plt.ylabel ('Z', fontsize =22)
plt.xlim((-1.2, 1.2))
plt.ylim((-1.4, 1.4))
plt.title ('Triangularity Derivative',fontsize = 20 )

plt.xticks(fontsize=18) 
plt.yticks(fontsize=18) 

plt.grid(True)
plt.legend()
plt.show()
