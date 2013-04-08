# Brain
# Handles the AI basically

from fans import *
from eyes import *
from time import sleep
from time import clock

class Brain:
	def __init__(self):
		self.fans = Fans()
		self.eyes = Eyes()
		print "Init brain"
		print "Running movement fans"
		sleep(2)


		target_time = time.clock() + 5

		while time.clock < target_time:
			self.fans.blow(range(5))
			sleep(0.1)
			print "Iterating"

		self.fans.all_off()
