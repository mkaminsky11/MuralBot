import sys
import time
import random
import pigpio

gpio_num = 4 # where connected

pi = pigpio.pi()

if not pi.connected:
	exit()
else:
	# all good, keep going
	pi.set_servo_pulsewidth(gpio_num, 1000)