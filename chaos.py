######################################################################################################################
# Name: Noah Jones
# Date: 9/30/2021
# Description: choas game
######################################################################################################################

#importing necessary libraries
import math
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


#class holding our canvas and necessary functions to plot the sierpinski triangle
class Chaos(Canvas):
	def __init__(self, window):
		self.window = window

	#function to plot colored points on the Tkinter canvas
	def plotPoints(self, limit):

		#setting our canvas to the original tkinter window and giving it client specified parameters
		C = Canvas(self.window, bg="white", height = 520, width = 600)
		
		#creating verticies objects to hold our base plot points
		v1= Point(294, 2)
		v2= Point(5, 510)
		v3= Point(595, 510)
		C.create_oval(v1.x, v1.y, v1.x+5, v1.y+5, outline="red", fill="red")
		C.create_oval(v2.x, v2.y, v2.x+5, v2.y-5, outline="red", fill="red")
		C.create_oval(v3.x, v3.y, v3.x-5, v3.y-5, outline="red", fill="red")
		C.pack()


		#getting our new midpoint
		basepoints = [v1, v2, v3]
		basepoint1, basepoint2 = random.choices(basepoints, k = 2)
		NewPlot= basepoint1.midpt(basepoint2)
		C.create_oval(NewPlot.x, NewPlot.y, NewPlot.x, NewPlot.y, outline="black", fill="black")
		#packing our pixel to the tkinter string
		C.pack()

		#while loop to plot number of points(limit)
		while limit > 0:
			
			#ramdom verticie picked from list
			V = random.choice(basepoints)

			#The newnewplot is the midpoint of a random verticie and our previously created new point otherwise knonw as NewPlot
			NewNewPlot= V.midpt(NewPlot)

			#Setting the new midpoint as the base point to be used in the midpoint formula with the randomly selected verticie 
			NewPlot = NewNewPlot
			C.create_oval(NewNewPlot.x, NewNewPlot.y, NewNewPlot.x, NewNewPlot.y, outline="black", fill="black")
			#packing our pixel to the tkinter string
			C.pack()
			#taking away number of points to be plotted 
			limit -= 1





##############
#MAIN PROGRAM
##############
#window parameters
WIDTH = 800
HEIGHT = 800
NUM_POINTS = 50000
# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("THE CHAOS GAME")
# create the coordinate system as a Tkinter canvas inside the window
s = Chaos(window)
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()