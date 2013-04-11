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

		# Grab the box
		self.arms.open_arms()
		sleep(1)
		self.arms.grab_pos()
		sleep(1)
		self.arms.grab()
		sleep(1)
		self.arms.rest_pos()

		sleep(2)

		# Put on pedastal
		self.arms.pedastal_pos()
		sleep(1)
		self.arms.open_arms()

		self.die()

	def die(self):
		sleep(0.5)
		self.robot.power._set_motor_rail(False)
