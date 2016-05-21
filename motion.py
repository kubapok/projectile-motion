import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math, sys

#zmienne


angle = math.radians(int(sys.argv[1]))


r = 0.2
kappa = 0.45 *np.pi * r*r * 0.6
m = 0.3
g = 9.81
v = 30
t = 0.05

#inicjalizacja
x = [0,]
y = [0,]
vx = [v*math.cos(angle),]
vy = [v*math.sin(angle),]

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

scale_len = int(1.4 * max (x + y))
ax.set_xlim(0, scale_len)
ax.set_ylim(0, scale_len)

ani = animation.FuncAnimation(fig, animate, interval=80, blit=True)
plt.show()
