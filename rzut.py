import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(-1.1, 1.1)


kappa = 2

def xpos(t):
	return t

def ypos(t):
	return np.sin(t/20)


def animate(t):
	x = np.arange(0,t, 0.01)
	line = ax.plot(x, ypos(x), color = 'b')
	return line

ani = animation.FuncAnimation(fig, animate, np.arange(1, 100),
    interval=25, blit=True)

plt.show()
