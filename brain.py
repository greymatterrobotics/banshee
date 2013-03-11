# Brain
# Handles the AI basically

from fans import *
from eyes import *

class Brain:
	def __init__(self):
		self.fans = Fans()
		self.eyes = Eyes()
		print "Init brain"
