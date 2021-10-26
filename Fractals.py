######################################################################################################################
# Name: Noah Jones
# Date: 10/25/21
# Description: choas game with additional shapes
######################################################################################################################
from point import Point
from tkinter import *
import math


class Fractal(Point, Canvas):
	def __init__(self, canvas, shape, dimensions):
		self.shape = shape
		self.dimensions = dimensions
		self.canvas = canvas

		def frac_x(r):
			return int((self.dimensions["max-x"] - \
				self.dimensions["min-x"]) * r) + \
				self.dimensions["min-x"]

		def frac_y(r):
			return int((self.dimensions["max-y"] - \
				self.dimensions["min-y"]) * r) + \
				self.dimensions["min-y"]

		if self.shape == "SierpinskiTriangle":
			self.r = 0.5
			v1 = Point(self.dimensions["mid-x"], self.dimensions["min-y"])
			v2 = Point(self.dimensions["min-x"], self.dimensions["max-y"])
			v3 = Point(self.dimensions["max-x"], self.dimensions["max-y"])
			self.Vs = [v1, v2, v3]
			self.numpoints=50000

		if self.shape == "Hexagon":
			self.r = 0.665
			v1 = Point(self.dimensions["min-x"], self.dimensions["height"]*.5)
			v2 = Point(self.dimensions["width"]*.25, self.dimensions["min-y"])
			v3 = Point(self.dimensions["width"]*.75, self.dimensions["min-y"])
			v4 = Point(self.dimensions["max-x"], self.dimensions["height"]*.5)
			v5 = Point(self.dimensions["width"]*.25, self.dimensions["max-y"])
			v6 = Point(self.dimensions["width"]*.75, self.dimensions["max-y"])
			self.Vs = [v1,v2,v3,v4,v5,v6]
			self.numpoints=50000
		
		if self.shape == "Pentagon":
			self.r = 0.618
			v1 = Point(self.dimensions["mid-x"]*2*cos(2*pi/5+60), (frac_y(0.5375)+self.dimensions["mid-y"]*sin(2*pi/5+60)))
			v2 = Point(self.dimensions["mid-x"]*2*cos(4*pi/5+60), (frac_y(0.5375)+self.dimensions["mid-y"]*sin(4*pi/5+60)))
			v3 = Point(self.dimensions["mid-x"]*2*cos(6*pi/5+60), (frac_y(0.5375)+self.dimensions["mid-y"]*sin(6*pi/5+60)))
			v4 = Point(self.dimensions["mid-x"]*2*cos(8*pi/5+60), (frac_y(0.5375)+self.dimensions["mid-y"]*sin(8*pi/5+60)))
			v5 = Point(self.dimensions["mid-x"]*2*cos(10*pi/5+60), (frac_y(0.5375)+self.dimensions["mid-y"]*sin(10*pi/5+60)))
			self.Vs=[v1,v2,v3,v4,v5]
			self.numpoints=50000

		if self.shape == "SierpinskiCarpet":
			self.r = 0.66
			v1=Point(self.dimensions["min-x"], self.dimensions["min-y"])
			v2=Point(self.dimensions["mid-x"], self.dimensions["min-y"])
			v3=Point(self.dimensions["max-x"], self.dimensions["min-y"])
			v4=Point(self.dimensions["min-x"], self.dimensions["mid-y"])
			v5=Point(self.dimensions["max-x"], self.dimensions["mid-y"])
			v6=Point(self.dimensions["min-x"], self.dimensions["max-y"])
			v7=Point(self.dimensions["mid-x"], self.dimensions["max-y"])
			v8=Point(self.dimensions["max-x"], self.dimensions["max-y"])
			self.numpoints=100000
			self.Vs=[v1,v2,v3,v4,v5,v6,v7,v8]

		if self.shape == "Octagon":
			self.r =0.705
			v1=Point(frac_x(0.2925),self.dimensions["min-y"])
			v2=Point(frac_x(0.7075),self.dimensions["min-y"])
			v3=Point(self.dimensions["min-x"], frac_y(0.2925))
			v4=Point(self.dimensions["max-x"], frac_y(0.2925))
			v5=Point(self.dimensions["min-x"], frac_y(0.7075))
			v6=Point(self.dimensions["max-x"], frac_y(0.7075))
			v7=Point(frac_x(0.2925), self.dimensions["max-y"])
			v8=Point(frac_x(0.7075), self.dimensions["max-y"])
			self.numpoints=75000
			self.Vs=[v1,v2,v3,v4,v5,v6,v7,v8]
			

#############
#MAIN PROGRAM
#############
"""
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the implemented fractals
FRACTALS = [ "SierpinskiTriangle", "SierpinskiCarpet",\

"Pentagon", "Hexagon", "Octagon" ]

# create the fractals in individual (sequential) windows
for f in FRACTALS:
	window = Tk()
	window.geometry("{}x{}".format(WIDTH, HEIGHT))
	window.title("The Chaos Game...Reloaded")
	# create the game as a Tkinter canvas inside the window
	s = ChaosGame(window)
	# make the current fractal
	s.make(f)
	# wait for the window to close
	window.mainloop()"""

