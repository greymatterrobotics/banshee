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
		print "Running lift fan"
		self.fans.lift()
		sleep(1)
		print "Forwards"
		self.fans.spin()
		sleep(5)
		self.fans.stop()
