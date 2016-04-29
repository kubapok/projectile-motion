import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(-1.1, 1.1)

def animate(i):
	x = np.arange(0,(0.01+0.01*i)*np.pi, 0.01)
	line = ax.plot(x, np.sin(x), color = 'b')
	return line

ani = animation.FuncAnimation(fig, animate, np.arange(1, 100),
    interval=25, blit=True)

plt.show()
