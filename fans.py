# Fans
# Handles all the fan shit like moving and blowing

from banshee import *
from time import sleep

class Fans:
	def __init__(self):
		self.r = Banshee()

		# Init ESC
		self.r.power._set_motor_rail(False)
		sleep(0.5)
		self.stop() # Ensure the ESCs are set to off pos
		self.r.power._set_motor_rail(True)
		sleep(6)
		print "Init fans"

	# Motor helpers
	def off(self, motor):
		self.r.servos[0][motor] = 53

	def stop(self):
		for i in range(5):
			self.off(i)

	def blow(self, motors):
		for i in motors:
			sleep(0.1)
			self.r.servos[0][i] = 59

	def suck(self, motors):
		for i in motors:
			self.r.servos[0][i] = 47


	# Movement helpers
	def backwards(self):
		self.blow([0, 1])

	def forwards(self):
		self.suck([0, 1])

	def left(self):
		self.blow([2, 3])

	def right(self):
		self.suck([2, 3])


	# Lift helpers
	def lift(self):
		self.r.servos[0][4] = 64
		sleep(0.5)
