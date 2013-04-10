# Brain
# Handles the AI basically

from sr import *
from fans import *
from eyes import *
from arms import *
from time import sleep, time

class Brain:
	def __init__(self):
		self.robot = Robot()
		self.arms = Arms(self.robot)
		self.eyes = Eyes(self.robot)
		self.fans = Fans(self.robot)

		self.fans.lift()
		sleep(1)
		self.fans.forwards()
		sleep(5)
		self.fans.stop()

		sleep(1)

		self.die()

	def die(self):
		sleep(0.5)
		self.robot.power._set_motor_rail(False)

	def test_encoder(self):
		acount = 0
		bcount = 0
		while True:
			acount = acount + self.robot.io[0].input[0].d
			bcount = bcount + self.robot.io[0].input[1].d
			print acount
			print bcount
			print ""
