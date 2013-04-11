# Eyes
# Handles vision stuff like seeing
from collections import namedtuple
import math

class Eyes:
	def __init__(self, robot):
		self.r = robot
		self.point = namedtuple('Point', ['x', 'y'])
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

	def arena_position(self):
		#Calculates the position of the robot in the arena by using arena markers as known points
		#Based off of maths outlined here: http://i.imgur.com/bTPAhAF.png
		#Coordinates are in metres from the top left of the arena (Northwest of the diagram on pg. 14 of the rulebook: https://www.studentrobotics.org/resources/2013/rulebook.pdf)

		markers = self.r.see()
		positions = []
		for m in markers:
			if m.info.marker_type == MARKER_ARENA:
				m_coords = arena_marker_coords(m.info.code)
				positions.append(self.point(math.sin(m.rot_y) * m.dist) + m_coords.x, math.cos(m.rot_y) * m.dist + m_coords.y)
		for p in positions:
			sum_x += p.x
			sum_y += p.y

		if len(positions) > 0:
			return self.point(sum_x / len(positions), sum_y / len(positions))
		else:
			return None


	def arena_marker_coords(self, marker_number):
		#Simple function to give arena coordinates of an arena marker.

		if 0 <= marker_number <= 6:
			return self.point(0, marker_number + 1)
		elif 7 <= marker_number <= 13:
			return self.point(marker_number - 6, 8)
		elif 14 <= marker_number <= 20:
			return self.point(8, 7 - (marker_number - 14) # Numbers from top to bottom are 20...14, we want to return 1...7. marker_number - 14 gives 6...0, 7 - (6...0) gives 1...7
		elif 21 <= marker_number <= 27:
			return self.point(7 - (marker_number - 21), 0) # Numbers from left to right are 27...21, we want to return 1...7. marker_number - 21 gives 6...0, 7 - (6...0) gives 1...7
		else:
			raise Exception("Passed marker number not that of an arena marker")