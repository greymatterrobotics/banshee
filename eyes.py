class Eyes:
	def __init__(self, robot):
		self.r = robot

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
