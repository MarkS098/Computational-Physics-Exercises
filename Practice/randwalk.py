import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

L = 101
lattice = np.zeros([L,L])
fig, ax = plt.subplots(figsize = (8,8))


# possible directions
dirs = np.array([[0,1],[0,-1],[1,0],[-1,0]])

# array to hold all locations visited during the random walk
locations = np.zeros((1,2))


def animate(i):
    global locations
    global L
    
    # first frame is handled separately
    if i == 0:
      line, = ax.plot([], [], lw=2)
      ax.plot(0,0,'ro')
      return line
    
    # generate a step of the random walk
    r = np.random.randint(4)
    move = dirs[r]
    nextloc = [locations[-1] + move]
    
    # if we reach the limit at L try again
    while nextloc > int(np.floor(L/2)) or nextloc < -int(np.floor(L/2)):
        r = np.random.randint(4)
        move = dirs[r]
        nextloc = [locations[-1] + move]
        
    locations = np.append(locations, nextloc, axis=0)
    
    # set the plot data
    xdata = locations[:,0]
    ydata = locations[:,1]
    
    ax.cla() # clear the previous plot (necessary for removing old dots)
    
    # update the plot limits
    ax.set_xlim(min(-L/2,min(xdata)-1), max(L/2,max(xdata)+1))
    ax.set_ylim(min(-L/2,min(ydata)-1), max(L/2,max(ydata)+1))
    
    # redraw the plot
    line, = ax.plot([], [], lw=2)
    line.set_data(xdata, ydata)
    ax.plot(locations[-1,0], locations[-1,1], 'ro')
    
    return line

anim = animation.FuncAnimation(fig, animate, frames=500, interval=100)
plt.show()