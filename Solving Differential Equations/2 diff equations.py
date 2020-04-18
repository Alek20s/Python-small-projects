# Solving a system of two differential equations of first order using  a 
# template with (odient), 

def lv(state, time, alpha, beta, gamma, delta):
    
    x = state[0]
    y = state[1]
    dxdt = -(2.7183**y)+(1-2*y)**(-0.5) # 1-st differential equation
    dydt = -x                           # 2-nd differenial equation
    return [dxdt, dydt]

from scipy.integrate import odeint
from numpy import linspace, zeros
initial = [0.001, 0.]       #initial conditions where E(0)=0.001 and F(0)=0
t = linspace(0, 40.0, 100)  # interval x in Debye length with numbers of steps
                                                                 
result = odeint(lv, initial, t, args=(8.0, 1.0, 3.0, 1.0))

import matplotlib.pyplot as plt           # plot

plt.plot(t, result[:, 0], label="Electric field")
plt.plot(t, result[:,1], label="Potential")
plt.legend()
plt.grid(which='major')
plt.show()

import matplotlib.pyplot as plt         # plot
j=zeros(shape=(len(result[:,1]),1))

for i in range(0,len(j)):
    j[i] = (17.11*2.7183**result[i,1])-1.0 # current= 17.11*exp(potential) -1
    
plt.plot (t,j, label="Current")             # plot
plt.legend()
plt.grid(which='major')
plt.show()