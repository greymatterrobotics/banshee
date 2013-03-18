# Banshee
# Wrapper around the Robot object to make it a singleton

from sr import *

class Banshee(Robot):
	_instance = None
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Banshee, cls).__new__(cls, *args, **kwargs)
		return cls._instance
