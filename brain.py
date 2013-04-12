# Brain
# Handles the AI basically

from sr import *
from fans import *
from eyes import *
from arms import *
from time import sleep, time

class Brain:
	def __init__(self):
		self.robot = Robot()
		self.arms = Arms(self.robot)
		self.eyes = Eyes(self.robot)
		#self.fans = Fans(self.robot)

		self.start()

		self.die()

	def die(self):
		sleep(0.5)
		self.robot.power._set_motor_rail(False)

	def start(self):
		pedestal_rot = False
		# Identity operator because it could return 0deg which is Falsey
		while pedestal_rot is False:
			pedestal = self.eyes.can_see_pedestal()
			print "Moving left"
			sleep(0.2)
			if pedestal is not False:
				pedestal_rot = pedestal['rot']

		print "Found a fucking pedestal!"

		# Align to the pedestal
		aligned = False
		while not aligned:
			pedestal_rot = self.eyes.pedestal_rotation(pedestal['id'])
			# Check we still have eyes on the marker
			if pedestal_rot > 11:
				print "Adjusting a little more left"
			elif pedestal_rot < -2:
				print "Overshot!! Adjusting back right"
			elif -2 < pedestal_rot < 11:
				print "aligned!"
				aligned = True
			else:
				print "Well something fucked up"

		# Move to the pedestal
		print "Turning off the lift fan"
		sleep(0.5)
		print "Going forwards"
		sleep(5)
		print "At pedestal"
		sleep(0.5)

		# Drop box onto thingy
		self.arms.pedestal_pos()

		# Clap hands


	def grab_place_box(self):
		# Grab the box
		self.arms.open_arms()
		sleep(1)
		self.arms.grab_pos()
		sleep(1)
		self.arms.grab()
		sleep(1)
		self.arms.rest_pos()

		sleep(2)

		# Put on pedastal
		self.arms.pedastal_pos()
		sleep(1)
		self.arms.open_arms()
