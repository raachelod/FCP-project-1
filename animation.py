#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:50:12 2022

@author: rachelodwyer
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# Finding itinital population N
N = int(input("Type your inital population, N")) #population - command line argument
# Initial number of infected people I0
I0 = int(input("How many people initally infected?"))  #infection - command line argument
# Initial number of recovered people R0
R0 = 0
# Resulting population initally susceptible
S0 = N - I0 - R0
# Contact rate (contact_rate), and average recovery rate (recovery_rate) (in 1/days).
contact_rate = 0.2
recovery_rate = 1/10
# A grid of time points (in days)
t_span = np.linspace(0, 100, 100) 
h = t_span[1]-t_span[0]
 
 
# Differential equations to model SIR.
def deriv(y, N, contact_rate, recovery_rate):
    S, I, R = y
    dSdt = -contact_rate * S * I / N
    dIdt = contact_rate * S * I / N - recovery_rate * I
    dRdt = recovery_rate * I
    return np.array([dSdt, dIdt, dRdt])
     
 
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
line = [ax.plot([], [], 'b', alpha=0.5, lw=2, label='Susceptible')[0]]
line.append(ax.plot([], [], 'r', alpha=0.5, lw=2, label='Infected')[0])
line.append(ax.plot([], [], 'g', alpha=0.5, lw=2, label='Recovered')[0])
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,1.2)
ax.set_xlim(0,len(t_span))
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(visible=True, which='major', c='w', lw=1.5, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
    
X = np.empty((3,len(t_span)))*np.nan
X[:,0] = (S0,I0,R0)

#def dataframe(): #trying to put the data into a data frame
# rng = pd.date_range('19-03-2020', periods = 748, freq= 'D')
# df = ({'Date':rng, 'No. hospital admissions': 'Infected'})
# df.to_csv = ('FCP-project-1/simulation_data.csv')
# print(df)

# initialization function: plot the background of each frame
def init():
    [line[i].set_data([], []) for i in range(3)]
    return line
 
#animation function.  
def animate(i):
    dX = deriv(X[:,i],N,contact_rate,recovery_rate)
    X[:,i+1] = X[:,i] + h*dX
   
    line[0].set_data(t_span, X[0,:]/1000)
    line[1].set_data(t_span, X[1,:]/1000)
    line[2].set_data(t_span, X[2,:]/1000)
    return line
 
anim =FuncAnimation(fig, animate, init_func=init,
                               frames=len(t_span)-1, interval=20, blit=True)


#creating grid animation 
#potentially create barchart
#create a specific animation that simulates the specific values from 'England' data 


    

plt.show()
plt.savefig('practicesaving')
plt.show()

#dataframe()

## 