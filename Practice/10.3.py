import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import animation

L = 101 # size of lattice
fig,ax = plt.subplots()
ax.set_xlim(L/2,-L/2)
ax.set_ylim(L/2,-L/2)

dirs = np.array([[1,0],[-1,0],[0,1],[0,-1]]) # possible directions
locations = np.zeros((1,2)) # array to store locations

def run(i):
    global locations
    global L
    
    # initial frame
    if i==0:
        line, = ax.plot([], [], lw = 2)
        ax.plot(0,0,'ro')
        return line
    
    valid_move = False
    while not valid_move:
      # generating a random step
      r = random.randrange(4)
      move = dirs[r]
      nextloc = [locations[-1] + move]
      
      # Check if the next location is within bounds
      if np.all(np.abs(nextloc) <= L/2):
          valid_move = True
    
    locations = np.append(locations, nextloc, axis = 0)
    
    # set the plot data
    xdata = locations[:,0]
    ydata = locations[:,1]
    
    ax.cla()
    
    # plot limits
    ax.set_xlim(L/2,-L/2)
    ax.set_ylim(L/2,-L/2)
    
    # redraw the plot
    line, = ax.plot([], [], lw=2)
    line.set_data(xdata, ydata)
    ax.plot(locations[-1,0], locations[-1,1], 'ro')
        
    return line

anim = animation.FuncAnimation(fig, run, frames=500, interval=100)
plt.show()    