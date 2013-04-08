# Brain
# Handles the AI basically

from fans import *
from eyes import *
from time import sleep, time

class Brain:
	def __init__(self):
		self.fans = Fans()
		self.eyes = Eyes()
		print "Init brain"
		print "Running movement fans"
		sleep(2)


		self.fans.forwards()
		sleep(5)

		self.fans.stop()
