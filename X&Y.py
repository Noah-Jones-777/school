######################################################################################################################
# Name: Noah Jones
# Date: 9/13/2021
# Description: program to do simple X & Y coordinate calculations such as midpoint and distance between two points
######################################################################################################################

#importing math for program calculations
import math

# the 2D point class
class Point:
	
	#class constructor with default values set at 0
	def __init__(self, x=0, y=0):
		self.x = x 
		self.y = y

		
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
		

	"""#function to retrive apporaiate coordinates in the needed mathematical expression
	def Coordinate_Retriver(self, set1, set2):
		x1, x2 = set1.x, set2.x
		y1, y2 = set1.y, set2.y
		return x1, y1, x2, y2"""


	#class method to calculate midpoint
	def midpt(set1, set2):
	
		x1, x2 = set1.x, set2.x
		y1, y2 = set1.y, set2.y

		#algorithm for the midpoint coordinates
		midpointX, midpointY = (((x1 + x2) / 2), ((y1 + y2) / 2))
		return(midpointX, midpointY)


	#class method to calculate distance between two points
	def dist(set1, set2):

		x1, x2 = set1.x, set2.x
		y1, y2 = set1.y, set2.y

		#algorithm for distance between two points
		partx = ((x2-x1)**2)
		party = ((y2-y1)**2)
		to_be_squared = partx + party
		distance = math.sqrt(to_be_squared)
		return ("{}".format(distance))

	#string
	def __str__(self):
		return(" ({}, {})".format(self.x, self.y))





##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print("p1:", p1)
print("p2:", p2)
print("p3:", p3)
# calculate and display some distances
print("distance from p1 to p2:", p1.dist(p2))
print("distance from p2 to p3:", p2.dist(p3))
print("distance from p1 to p3:", p1.dist(p3))
# calculate and display some midpoints
print("midpt of p1 and p2:", p1.midpt(p2))
print("midpt of p2 and p3:", p2.midpt(p3))
print("midpt of p1 and p3:", p1.midpt(p3))
# just a few more things...
p4 = p1.midpt(p3)
print("p4:", p4)
print("distance from p4 to p1:", p4.dist(p1))
