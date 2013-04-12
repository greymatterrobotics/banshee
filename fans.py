# Fans
# Handles all the fan shit like moving and blowing

from time import sleep

class Fans:
	def __init__(self, robot):
		self.r = robot

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
		for x in range(106, 121):
			for i in motors:
				self.r.servos[0][i] = float(x) / 2
				sleep(0.01)

	def suck(self, motors):
		for x in range(106, 75, -1):
			for i in motors:
				self.r.servos[0][i] = float(x) / 2
				sleep(0.01)


	# Movement helpers
	def backwards(self):
		self.lift()
		self.blow([0, 1])

	def forwards(self):
		self.suck([0, 1])
		sleep(1)
		self.lift()

	def left(self):
		self.lift()
		self.blow([2, 3])

	def right(self):
		self.lift()
		self.suck([2, 3])


	# Lift helpers
	def lift(self):
		self.r.servos[0][4] = 65
		sleep(0.5)
