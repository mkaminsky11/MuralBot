import sys
import time
import random
import pigpio

gpio_num = [3,4] # where connected

pi = pigpio.pi()

if not pi.connected:
	print("exit")
	exit()
else:
	# all good, keep going
	for n in gpio_num:
		pi.set_servo_pulsewidth(n, 1000)
	time.sleep(5)
	for n in gpio_num:
		pi.set_servo_pulsewidth(n, 2000)
	time.sleep(5)
	for n in gpio_num:
		pi.set_servo_pulsewidth(n, 1500)

# 1000 = fast one way
# 1500 = stop
# 2000 = fast the other way