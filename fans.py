# Fans
# Handles all the fan shit like moving and blowing

from banshee import *
from time import sleep

class Fans:
	def __init__(self):
		self.r = Banshee

		# Init ESC
		#self.r.power._set_motor_rail(False)
		#sleep(0.5)
		#self.all_off()
		#self.r.power._set_motor_rail(True)
		#sleep(6)
		print "Init fans"

	# Motor helpers
	def all_off(self):
		for i in range(4):
			self.r.servos[0][i] = 53

	def blow(self, motors):
		for i in motors:
			self.r.servos[0][i] = 59

	def suck(self, motors):
		for i in motors:
			self.r.servos[0][i] = 47

	# Movement helpers
	def forwards(self):
		self.blow([0, 1])
		self.suck([2, 3])

	def backwards(self):
		self.blow([2, 3])
		self.suck([0, 1])

	def stop(self):
		self.all_off()
