######################################################################################################################
# Name: Noah Jones
# Date: 10/25/21
# Description: Fractal and Point class with additional Fractal sublclasses
######################################################################################################################
from tkinter import *
import math


# the 2D point class
class Point:
	
	#class constructor with default values set at 0
	def __init__(self, x=0, y=0):
		self.x = float(x) 
		self.y = float(y)

	#acessor
	@property
	def x(self):
		return self._x

	#mutator
	@x.setter
	def x(self, value):
		self._x = value

	#acessor
	@property
	def y(self):
		return self._y

	#mutator
	@y.setter
	def y(self, value):
		self._y = value
		
	#class method to calculate midpoint
	def midpt(set1, set2):
	
		#get necessary point data for calculations
		x1, x2 = set1.x, set2.x
		y1, y2 = set1.y, set2.y

		#algorithm for the midpoint coordinates
		midpointX, midpointY = (((x1 + x2) / 2), ((y1 + y2) / 2))

		#creating new Point object to in order for new object to use further distance method
		new_obj = Point(midpointX, midpointY)
		return new_obj

	#class method to calculate distance between two points
	def dist(set1, set2):

		#get necessary point data for calculations
		x1, x2 = set1.x, set2.x
		y1, y2 = set1.y, set2.y

		#algorithm for distance between two points
		partx = ((x2-x1)**2)
		party = ((y2-y1)**2)
		to_be_squared = partx + party
		distance = math.sqrt(to_be_squared)
		return distance

	def interpt(self, other, r):
		#the x-component
		rx = r 
		if (self.x > other.x):
			rx = 1.0 - r 
		#the y-component
		ry = r
		if (self.y > other.y):
			ry = 1.0 - r 

		x = abs(self.x-other.x)* rx + min(self.x, other.x)
		y = abs(self.y - other.y) * ry + min(self.y, other.y)
		return Point(x,y)

	#magic function to dictate how the object will be printed out
	def __str__(self):
		return(" ({},{})".format(self.x, self.y))


#The Fractal class
class Fractal(Point, Canvas):
	def __init__(self, canvas, dimensions):
		#dimensions is the dictionary provided by the chaos game
		self.dimensions = dimensions
		self.canvas = canvas

	def frac_x(self, r):
		return int((self.dimensions["max-x"] - \
			self.dimensions["min-x"]) * r) + \
			self.dimensions["min-x"]

	def frac_y(self, r):
		return int((self.dimensions["max-y"] - \
			self.dimensions["min-y"]) * r) + \
			self.dimensions["min-y"]

#Triangle Fractal sublcass
class SierpinskiTriangle(Fractal):
	def __init__(self, canvas, dimensions):
		#using Fractal __init__ treatment of canvas and dimensions
		super().__init__(canvas, dimensions)
		self.r = 0.5
		v1 = Point(self.dimensions["mid-x"], self.dimensions["min-y"])
		v2 = Point(self.dimensions["min-x"], self.dimensions["max-y"])
		v3 = Point(self.dimensions["max-x"], self.dimensions["max-y"])
		self.Vs = [v1, v2, v3]
		self.numpoints=50000

#Hexagon Fractal sublclass
class Hexagon(Fractal):
	def __init__(self, canvas, dimensions):
		super().__init__(canvas, dimensions)
		self.r = 0.665
		v1 = Point(self.dimensions["mid-x"], self.dimensions["min-y"])
		v2 = Point(self.dimensions["min-x"], self.frac_y(0.25))
		v3 = Point(self.dimensions["max-x"], self.frac_y(0.25))
		v4 = Point(self.dimensions["min-x"], self.frac_y(0.75))
		v5 = Point(self.dimensions["max-x"], self.frac_y(0.75))
		v6 = Point(self.dimensions["mid-x"], self.dimensions["max-y"])
		self.Vs = [v1,v2,v3,v4,v5,v6]
		self.numpoints=50000
		
#Pentagon Fractal subclass
class Pentagon(Fractal):
	def __init__(self, canvas, dimensions):
		super().__init__(canvas, dimensions)
		self.r = 0.618
		#This a variable to hold mid-x + mid-x so the statement is not as large
		Dmidx = self.dimensions["mid-x"] * 2
		v1 = Point(Dmidx*math.cos(2*math.pi/5+60),\
		 (self.frac_y(0.5375)+self.dimensions["mid-y"]*math.sin(2*math.pi/5+60)))

		v2 = Point(Dmidx*math.cos(4*math.pi/5+60),\
		 (self.frac_y(0.5375)+self.dimensions["mid-y"]*math.sin(4*math.pi/5+60)))

		v3 = Point(Dmidx*math.cos(6*math.pi/5+60),\
		 (self.frac_y(0.5375)+self.dimensions["mid-y"]*math.sin(6*math.pi/5+60)))

		v4 = Point(Dmidx*math.cos(8*math.pi/5+60),\
		 (self.frac_y(0.5375)+self.dimensions["mid-y"]*math.sin(8*math.pi/5+60)))

		v5 = Point(Dmidx*math.cos(10*math.pi/5+60),\
		 (self.frac_y(0.5375)+self.dimensions["mid-y"]*math.sin(10*math.pi/5+60)))
		self.Vs=[v1,v2,v3,v4,v5]
		self.numpoints=50000

#Square Fractal sublcass
class SierpinskiCarpet(Fractal):
	def __init__(self, canvas, dimensions):
		super().__init__(canvas, dimensions)
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

#Octagon Fractal subclass
class Octagon(Fractal):
	def __init__(self, canvas, dimensions):
		super().__init__(canvas, dimensions)
		self.r =0.705
		v1=Point(self.frac_x(0.2925),self.dimensions["min-y"])
		v2=Point(self.frac_x(0.7075),self.dimensions["min-y"])
		v3=Point(self.dimensions["min-x"], self.frac_y(0.2925))
		v4=Point(self.dimensions["max-x"], self.frac_y(0.2925))
		v5=Point(self.dimensions["min-x"], self.frac_y(0.7075))
		v6=Point(self.dimensions["max-x"], self.frac_y(0.7075))
		v7=Point(self.frac_x(0.2925), self.dimensions["max-y"])
		v8=Point(self.frac_x(0.7075), self.dimensions["max-y"])
		self.numpoints=75000
		self.Vs=[v1,v2,v3,v4,v5,v6,v7,v8]
