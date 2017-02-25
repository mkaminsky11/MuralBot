import sys
import time
import random
import pigpio

gpio_num = 4 # where connected

pi = pigpio.pi()

if not pi.connected:
	print("exit")
	exit()
else:
	# all good, keep going
	pi.set_servo_pulsewidth(gpio_num, 1000)
	time.sleep(5)
	pi.set_servo_pulsewidth(gpio_num, 2000)
	time.sleep(5)
	pi.set_servo_pulsewidth(gpio_num, 1500)

# 1000 = fast one way
# 1500 = stop
# 2000 = fast the other way