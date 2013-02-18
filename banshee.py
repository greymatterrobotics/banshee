from sr import *
from fans import *
from eyes import *
from sensors import *

class Banshee:
	def __init__(self):
		self.r = Robot()

		self.fans = Fans(self.r)
		self.eyes = Eyes(self.r)
		self.sensors = Sensors()
		print "Robot initialised"
