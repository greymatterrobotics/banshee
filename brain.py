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
		sleep(3)
		self.fans.blow([0, 1])
		sleep(3)
		self.fans.all_off()
		sleep(2)
		self.fans.blow([2, 3])
		sleep(3)
		self.fans.all_off()