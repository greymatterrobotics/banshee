# Arms
# Handles grabber etc.

from time import sleep

class Arms:
	def __init__(self, robot):
		self.r = robot

	# Move arm to the forward facing grab position
	def grab_pos(self):
		self.r.motors[0].target = -20
		sleep(0.1)
		while not self.r.io[0].input[0].d:
			sleep(0.05)
		self.r.motors[0].target = 0
		sleep(0.5)
		# Compensate
		self.r.motors[0].target = 20
		sleep(0.5)
		self.r.motors[0].target = 0

	def open_arms(self):
		self.r.servos[0][5] = 70
		self.r.servos[0][6] = 25
		sleep(0.5)

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
		self.r.motors[0].target = 20
		sleep(1)
		while not self.r.io[0].input[0].d:
			sleep(0.05)
		self.r.motors[0].target = 0
		sleep(0.5)
		# Compensate
		self.r.motors[0].target = -20
		sleep(0.5)
		self.r.motors[0].target = 0
