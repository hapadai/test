# -*- coding: euc-kr -*-

class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def get(self):
		return "(" + str(self.x) +","+ str(self.y) + ")"
	
	def __add__(self, other):
		newX = self.x + other.x
		newY = self.y + other.y
		return Point(newX, newY)
