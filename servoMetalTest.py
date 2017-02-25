#import sys
import time
#import random
import pigpio
#import atexit

gpio_num = 12 # where connected

pi = pigpio.pi()

#pi.set_mode(gpio_num, pigpio.OUTPUT) # Set gpio as an output.
#
if not pi.connected:
	print("exit")
	exit()
# all good, keep going
pi.set_servo_pulsewidth(gpio_num, 800)
time.sleep(0.3)
pi.set_servo_pulsewidth(gpio_num, 1500)
time.sleep(1)
pi.set_servo_pulsewidth(gpio_num, 0)
pi.stop()

# 1000 = fast one way
# 1500 = stop
# 2000 = fast the other way

#def exit_handler():
#	print('My application is ending!')
	#pi.set_servo_pulsewidth(gpio_num, 1500)

#atexit.register(exit_handler)
