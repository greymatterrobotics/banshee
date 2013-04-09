# Arms
# Handles grabber etc.

from time import sleep

class Arms:
	def __init__(self, robot):
		self.r = robot
		print "Init arms"

	def grab(self):
		self.r.servos[0][6]	= 50
		sleep(10)
