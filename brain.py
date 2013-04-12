# Brain
# Handles the AI basically

from sr import *
from fans import *
from eyes import *
from arms import *
from time import sleep, time

class Brain:
	def __init__(self):
		robot = Robot()
		self.arms = Arms(robot)
		self.eyes = Eyes(robot)
		self.fans = Fans(robot)

		while True:
			print self.eyes.arena_position()
