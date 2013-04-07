# Brain
# Handles the AI basically

from fans import *
from eyes import *
from time import sleep

class Brain:
	def __init__(self):
		self.fans = Fans()
		self.eyes = Eyes()
		print "Init brain"
		print "Running movement fans"
		self.fans.blow(range(5))
		sleep(3)
		self.fans.all_off()
