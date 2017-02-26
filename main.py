import time
import pigpio
import atexit
import config

pi = pigpio.pi()
if not pi.connected:
	print("exit")
	exit()
# all good, keep going

def s(pin, state):
	pi.set_servo_pulsewidth(pin, state)

def stopAll():
	s(config.d1_pin, 1500)
	s(config.d2_pin, 1500)

ok = True
started = False
stopped = False
while(ok):
	pressed = pi.read(config.b_pin) == 0
	#print(pi.read(config.b_pin))
	if pressed:
		if not started:
			started = True
			
			#
			# STRAIGHT
			#

			#s(config.d1_pin, 1171)
			#s(config.d2_pin, 2500)
			#time.sleep(4)
			
			# LEFT
			s(config.d1_pin, 1771)
			s(config.d2_pin, 2500)
			time.sleep(1.42)

			started = False
			stopAll()
			#ok = False
		#else:
		#	stopAll()
		#	ok = False
pi.stop()

def exit_handler():
	print('My application is ending!')
	
atexit.register(exit_handler)
