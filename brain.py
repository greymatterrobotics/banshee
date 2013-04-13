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
		self.fans = Fans(self.robot)

		self.start()
		#self.second_token()


		#self.fans.lift()
		#while True:
			#sleep(2)

		#self.shitty_comp_mode()

		self.die()

	def shitty_comp_mode(self):
		sleep(3)

		# Grip token
		self.arms.open_arms()
		print "About to grip"
		sleep(1)
		self.arms.grab()

		# Strafe left
		self.fans.left()
		sleep(4)
		self.fans.stop()
		sleep(1)

		self.fans.forwards()
		sleep(3)
		self.fans.stop()
		sleep(1)

		self.arms.pedestal_pos()
		sleep(1)
		self.arms.open_arms()

	def die(self):
		sleep(0.5)
		self.robot.power._set_motor_rail(False)

	def strafe_left_to_pedestal(self):
		self.fans.lift()
		pedestal_rot = False
		# Identity operator because it could return 0deg which is Falsey
		while pedestal_rot is False:
			pedestal = self.eyes.can_see_pedestal()
			self.fans.left()
			if pedestal is not False:
				pedestal_rot = pedestal['rot']
				self.fans.stop()
			sleep(0.2)

		self.align_with_marker(pedestal['id'])

	def start(self):
		# Grab box immediately
		self.arms.open_arms()
		print "About to grip"
		sleep(1)
		self.arms.grab()

		print "Moving forwards a bit"
		self.fans.forwards()
		sleep(2)
		self.fans.stop()
		sleep(1)

		print "Strafing left to pedestal"
		self.strafe_left_to_pedestal()

		# Move to the pedestal
		print "Move forwards to pedestal"
		self.fans.stop()
		sleep(0.5)
		self.fans.forwards()
		sleep(5)
		self.fans.stop()
		print "At pedestal"
		sleep(0.5)

		# Drop box onto thingy
		self.arms.pedestal_pos()
		self.arms.open_arms()
		sleep(2)

		# Clap hands

		# Return grabber to rest pos
		self.arms.rest_pos()

		print "Moving back a little"
		sleep(0.5)
		print "Rotating 180deg"
		sleep(2)

	def second_token(self):
		box = False
		while box is False:
			box = self.eyes.can_see_box()
			print "Can't see the fucking box!"

		self.align_with_marker(box['id'])

		sleep(0.5)
		print "Going forwards"
		sleep(5)
		print "at box"

		# Grab the nigga token
		self.arms.open_arms()
		self.arms.grab_pos()
		self.arms.grab()
		self.arms.rest_pos()

		sleep(1)
		print "Spin 180deg"
		sleep(2)

		self.strafe_left_to_pedestal()

		# Go to pedestal
		sleep(0.5)
		print "Going forwards"
		sleep(5)
		print "at pedestal"

		# Drop box onto thingy
		self.arms.pedestal_pos()
		self.arms.open_arms()
		sleep(2)

		self.arms.rest_pos()

	def align_with_marker(self, id):
		# Align to the pedestal
		aligned = False
		while not aligned:
			pedestal_rot = self.eyes.pedestal_rotation(id)
			# Check we still have eyes on the marker
			if pedestal_rot > 11:
				self.fans.left()
			elif pedestal_rot < -2:
				self.fans.right()
			elif -2 < pedestal_rot < 11:
				print "Aligned!"
				self.fans.stop()
				aligned = True
			else:
				print "Well something fucked up"


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

		# Put on pedestal
		self.arms.pedestal_pos()
		sleep(1)
		self.arms.open_arms()
