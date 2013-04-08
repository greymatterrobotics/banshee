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


		print "Forwards"
		self.fans.forwards()
		sleep(2)
		self.fans.stop()

		sleep(0.5)

		print "back"
		self.fans.backwards()
		sleep(2)
		self.fans.stop()

		sleep(0.5)

		print "left"
		self.fans.left()
		sleep(2)
		self.fans.stop()

		sleep(0.5)

		print "right"
		self.fans.right()
		sleep(2)
		self.fans.stop()

		sleep(0.5)
