######################################################################################################################
# Name: Noah Jones
# Date: 10/25/21
# Description: choas game with additional shapes
######################################################################################################################

#importing necessary libraries
from tkinter import *
import random
from Fractals import *

#class holding our canvas and necessary functions to plot the sierpinski triangle
class ChaosGame(Canvas):
	def __init__(self, window, plotcolor):
		self.window = window
		self.dimensions = {
		"width":600,
		"height":520,
		"min-x" : 5,
		"max-x":595,
		"mid-x":300,
		"min-y":5,
		"max-y":515,
		"mid-y":260
		}
		self.vertexradius = 2
		self.vertexcolor = "red"
		self.plotcolor = str(plotcolor)

	def make(self, shape):
		C = Canvas(self.window, bg = "white", height=self.dimensions["height"], width=self.dimensions["width"])
		#using the eval keyworkd since the fractal subclass constructor will be a string
		parameters = "{}(C, self.dimensions)".format(shape)
		F = eval(parameters)
		self.plotpoints(F, C)
	

	def plotpoints(self, fractal_obj, canvas_obj):
		for i in fractal_obj.Vs:
			canvas_obj.create_oval(i.x, i.y, i.x+self.vertexradius, i.y+self.vertexradius,\
			 outline=self.vertexcolor, fill=self.vertexcolor)
		#number of points to plot
		limit = fractal_obj.numpoints
		#our first two randomly selected verticies
		base_points = fractal_obj.Vs
		v1, v2 = random.choices(base_points, k = 2)
		temporary_point = v1.midpt(v2)
		canvas_obj.create_oval(temporary_point.x, temporary_point.y, temporary_point.x, temporary_point.y,\
		 outline="black", fill="black")
		#algorithm for plotting points using everything we've combined
		while limit > 0:
			random_v = random.choice(fractal_obj.Vs)
			new_point = temporary_point.interpt(random_v, fractal_obj.r)
			#plotting our point
			canvas_obj.create_oval(new_point.x, new_point.y, new_point.x, new_point.y,\
				outline=self.plotcolor, fill=self.plotcolor)
			temporary_point = new_point
			limit-=1
		canvas_obj.pack()


##############
#MAIN PROGRAM#
##############
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
#colors for fun
#excluding red to see verticies
colors = ["red", "blue", "black", "green", "pink", "orange", "yellow", "purple", "gray", "turquoise"]
Fractals = ["SierpinskiTriangle", "SierpinskiCarpet",\
"Pentagon", "Hexagon", "Octagon"]
for f in Fractals:
	random_color = random.choice(colors)
	window = Tk()
	window.geometry("{}x{}".format(WIDTH, HEIGHT))
	window.title("The Chaos Game...Reloaded")
	# create the game as a Tkinter canvas inside the window
	s = ChaosGame(window, random_color)
	# make the current fractal
	s.make(f)
	# wait for the window to close
	window.mainloop()