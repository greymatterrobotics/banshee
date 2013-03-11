# Eyes
# Handles vision stuff like seeing

from banshee import *

class Eyes:
	def __init__(self):
		self.r = Banshee
		print "Init eyes"

	def is_markers(self):
		markers = self.r.see()
		if len(markers) > 0:
			return True
		else:
			return False

	def marker_distance(self):
		while(True):
			markers = self.r.see()

			if len(markers) > 0:
				for marker in markers:
					return marker.dist
			else:
				return 0
