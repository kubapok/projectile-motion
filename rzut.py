import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

class animated_plot():
	def __init__(self):
		self.fig, self.ax = plt.subplots()
	def set_plot_dim(self, xliml = 0, xlimr = 100, ylimd = 0, ylimu = 2):
		self.ax.set_xlim(xliml, xlimr)
		self.ax.set_ylim(ylimd, ylimu)
	def set_time_range(self, left = 0, right = 100):
		self.t_left = 0
		self.t_right = 100
	def set_xpos_func(self, x_func):
		self.xpos = x_func
	def set_ypos_func(self, y_func):
		self.ypos = y_func
	def animate(self,t):
		x = np.arange(0,t, 0.01)
		line = self.ax.plot(x, self.ypos(x), color = 'b')
		return line
	def show(self,):
		ani = animation.FuncAnimation(self.fig, self.animate, np.arange(self.t_left, self.t_right),
		    interval=25, blit=True)
		plt.show()




my_plot = animated_plot()
my_plot.set_plot_dim(0,100, 0, 3)
my_plot.set_time_range()
def xpos(t):
	return t
my_plot.set_xpos_func(xpos)
def ypos(t):
	return np.sin(t/20)
my_plot.set_ypos_func(ypos)
my_plot.show()
