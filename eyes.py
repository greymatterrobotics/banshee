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
				if 0 <= m.info.code <= 6:
					positions.append(self.point(math.cos(m.rot_y) * m.dist, (math.sin(m.rot_y) * m.dist) + (m.info.code + 1))
				elif 7 <= m.info.code <= 13:
					positions.append(self.point((math.sin(m.rot_y) * m.dist) + (m.info.code - 6),8 - (math.cos(m.rot_y) * m.dist))
				elif 14 <= m.info.code <= 20:
					positions.append(self.point(8 - (math.cos(m.rot_y) * m.dist), (math.sin(m.rot_y) * m.dist) + (7 - (m.info.code - 14)))
				elif 21 <= m.info.code <= 27:
					positions.append(self.point((math.sin(m.rot_y) * m.dist) + (7 - (m.info.code - 21)), math.cos(m.rot_y) * m.dist)
				else
					raise Exception("Arena marker code not dealt with") #This should never be called. If it is, panic
		for p in positions:
			sum_x += p.x
			sum_y += p.y

		if len(positions) > 0:
			return self.point(sum_x / len(positions), sum_y / len(positions))
		else:
			return None