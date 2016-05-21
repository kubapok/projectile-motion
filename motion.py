import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

#zmienne
r = 0.2
kappa = 0.45 *np.pi * r*r * 0.6
m = 0.3
g = 9.81
t = 0.05

#inicjalizacja
x = [0,]
y = [0,]
vx = [10,]
vy = [30,]

#kolejne iteracje
while not y[-1] < 0:
	vx.append(vx[-1] -  t*(kappa/m)*np.sqrt( vx[-1]**2 + vy[-1]**2)*vx[-1]   )
	vy.append(vy[-1] -  t*( (kappa/m)*np.sqrt( vx[-1]**2 + vy[-1]**2)*vy[-1] + g)  )
	x.append(x[-1] +  vx[-2])
	y.append(y[-1] +  vy[-2])


def animate(t):
	line = ax.plot(x[0:t], y[0:t], color = 'b')
	return line


fig, ax = plt.subplots()

ax.set_xlim(0, int(1.4*x[-1]))
ax.set_ylim(0, int(1.4*max(y)))

ani = animation.FuncAnimation(fig, animate, interval=80, blit=True)
plt.show()
