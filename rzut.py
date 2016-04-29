import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


x = np.arange(0,2*np.pi, 0.01)        
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, 5)

def animate(i):
	x = np.arange(0,(0.01+0.01*i)*np.pi, 0.01)
	line = ax.plot(x, np.sin(x))
	return line

def init():
	x = np.arange(0,(0.01)*np.pi, 0.01)
	line = ax.plot(x, np.cos(x))
	return line


ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), 
init_func=init,
    interval=25, blit=True)
plt.show()
