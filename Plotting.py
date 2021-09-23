######################################################################################################################
# Name: Noah Jones
# Date: 9/21/21
# Description: program to randomly plot colored points on an XY GUI
######################################################################################################################
from tkinter import *
import random
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

	#magic function to dictate how the object will be printed out
	def __str__(self):
		return(" ({},{})".format(self.x, self.y))
	# write your code for the point class here (and subsequently remove this comment)

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
	def __init__(self, window):
		self.window = window

	def plotPoints(self, iterations):
		x = Canvas(self.window, bg="white", height = 800, width = 800)
		for i in range(10):
			x,y = random.randint(1,800),random.randint(1,800)
			x.create_oval(0,0,0,0, outline="black", fill="red", padx=x, pady=y)

		x.pack()
		
	# write your code for the coordinate system class here (and subsequently remove this comment)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()