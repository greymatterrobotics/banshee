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
		sleep(0.5)
		self.off([2])


	def left(self, first):

		self.lift()
		if first == 1:
			self.suck([3])
			self.blow([2])
		else:
			self.blow([2])
			self.suck([3])

		#self.blow([0])
		#self.suck([1])
		#sleep(0.2)
		#self.off([1])
		#self.off([0])

	def right(self):
		self.lift()
		if first == 1:
			self.blow([3])
			self.suck([2])
		else:
			self.suck([2])
			self.blow([3])


	# Lift helpers
	def lift(self):
		self.r.servos[0][4] = 67
		sleep(0.5)


	# Shift funcs
	def shift_left(self):
		self.left((0))
		sleep(1)
		self.stop()
		sleep(1)
		self.left((1))
		sleep(1)
		self.stop()

	def shift_right(self):
		self.right((0))
		sleep(1)
		self.stop()
		sleep(1)
		self.right((1))
		sleep(1)
		self.stop()