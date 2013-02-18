import serial

class Sensors:
	def __init__(self):
		self.ser = serial.Serial('/dev/ttyACM0', 19200)

	def get_accel(self):
		return self.ser.readline().strip().split(',')
