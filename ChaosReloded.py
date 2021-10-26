######################################################################################################################
# Name: Noah Jones
# Date: 10/25/21
# Description: choas game with additional shapes
######################################################################################################################

#importing necessary libraries
from tkinter import *
import random
from Fractals import Fractal
from point import Point





#class holding our canvas and necessary functions to plot the sierpinski triangle
class ChaosGame(Canvas):
	def __init__(self, window):
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
		self.pointcolor = "black"

	def make(self, shape):
		C = Canvas(self.window, bg = "white", height=self.dimensions["height"], width=self.dimensions["width"])
		F = Fractal(C, shape, self.dimensions)
		self.plotpoints(F, C)

	def plotpoints(self, fractal_obj, canvas_obj):
		for i in fractal_obj.Vs:
			canvas_obj.create_oval(i.x, i.y, i.x+2, i.y+2, outline="red", fill="red")
		canvas_obj.pack()
		limit = fractal_obj.numpoints
		v1 = random.choice(fractal_obj.Vs) 
		v2 = random.choice(fractal_obj.Vs)
		temporary_point = v1.midpt(v2)
		canvas_obj.create_oval(temporary_point.x, temporary_point.y, temporary_point.x, temporary_point.y, outline="black", fill="black")
		while limit > 0:
			random_v = random.choice(fractal_obj.Vs)
			new_point = temporary_point.midpt(random_v)
			canvas_obj.create_oval(new_point.x, new_point.y, new_point.x, new_point.y, outline="black", fill="black")
			temporary_point = new_point
			limit-=1
		canvas_obj.pack()




#test stuff
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520

window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game...Reloaded")
# create the game as a Tkinter canvas inside the window
s = ChaosGame(window)
# make the current fractal
s.make("Hexagon")
# wait for the window to close
window.mainloop()





"""
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
			"""
	






"""
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
window.mainloop()"""