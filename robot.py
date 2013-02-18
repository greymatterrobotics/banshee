from banshee import *

b = Banshee()

while(True):
	print b.sensors.get_accel()

def forwards_until_marker():
	while(True):
		if b.eyes.is_markers():
			b.fans.forwards()

			dist = b.eyes.marker_distance()
			print dist
			if dist < 1.0:
				b.fans.stop()
				break

		else:
			print "No markers"