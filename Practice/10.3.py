import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim

L = 101  # Size of the lattice
fig, ax = plt.subplots()
ax.set_xlim(-L/2, L/2)
ax.set_ylim(-L/2, L/2)

dirs = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])  # Possible directions
locations = np.zeros((1, 2))  # Array to store locations

def run(i):
    global locations
    global L

    # Initial frame is handled seperately
    if i == 0:
        line, = ax.plot([], [], lw=2)
        ax.plot(0, 0, 'ro')
        return line

    current_location = locations[-1]

    # Check if the particle is anchored to an edge
    if np.any(np.abs(current_location) >= L / 2 - 1):
        # If anchored, do not move further
        ax.cla()
        ax.set_xlim(-L/2, L/2)
        ax.set_ylim(-L/2, L/2)
        line, = ax.plot(locations[:, 0], locations[:, 1], lw=2)
        ax.plot(current_location[0], current_location[1], 'ro')
        return line

    valid_move = False
    while not valid_move:
        # Generating a random step
        r = random.randrange(4)
        move = dirs[r]
        nextloc = current_location + move

        # Check if the next location is within bounds
        if np.all(np.abs(nextloc) < L / 2):
            valid_move = True

    locations = np.append(locations, [nextloc], axis=0)

    # Set the plot data
    xdata = locations[:, 0]
    ydata = locations[:, 1]

    ax.cla()

    # Plot limits
    ax.set_xlim(-L/2, L/2)
    ax.set_ylim(-L/2, L/2)

    # Redraw the plot
    line, = ax.plot(xdata, ydata, lw=2)
    ax.plot(locations[-1, 0], locations[-1, 1], 'ro')

    return line


animate = anim.FuncAnimation(fig, run, frames=500, interval=100)
plt.show()