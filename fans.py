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
	def off(self, motors):
		for i in motors:
			self.r.servos[0][i] = 53

	def stop(self):
		self.off(range(5))

	def blow(self, motors):
		for x in range(110, 126):
			for i in motors:
				self.r.servos[0][i] = float(x) / 2
				sleep(0.01)

	def suck(self, motors):
		for x in range(106, 82, -1):
			for i in motors:
				self.r.servos[0][i] = float(x) / 2
				sleep(0.01)


	# Movement helpers
	def backwards(self):
		self.lift()
		self.suck([0])
		self.blow([1])

	def forwards(self):
		self.lift()
		self.blow([0])
		self.suck([1])
		self.suck([2])
		time.sleep(1)
		self.off([2])


	def left(self):
		self.lift()

	def right(self):
		self.lift()


	# Lift helpers
	def lift(self):
		self.r.servos[0][4] = 65
		sleep(0.5)
