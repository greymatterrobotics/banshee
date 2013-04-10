# Arms
# Handles grabber etc.

from time import sleep

class Arms:
	def __init__(self, robot):
		self.r = robot

	# Move arm to the forward facing grab position
	def grab_pos(self):
		# 60 is rotate forwards
		# 40 is rotate back
		self.r.servos[0][7] = 60
		sleep(1)
		self.r.servos[0][7] = 50
		sleep(0.2)

	def grab(self):
		# Move to 'grab rest' position (dead straight)
		self.r.servos[0][5] = 85
		self.r.servos[0][6] = 10
		sleep(0.5)
		# Grab and put pressure on the box
		self.r.servos[0][5] = 100
		self.r.servos[0][6] = 0
		sleep(0.5)

	# Move arm back to over the robot
	def rest_pos(self):
		self.r.servos[0][7] = 40
		sleep(5)
		self.r.servos[0][7] = 50
