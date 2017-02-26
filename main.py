import time
import pigpio
import atexit
import config

pi = pigpio.pi()
if not pi.connected:
	print("exit")
	exit()
# all good, keep going

turns = 0
t = 0
goalTime = 0

def goStr(tt):
	global goalTime
	global state
	global startTime
	state = 1
	startTime = time.time()
	s(config.d1_pin, 1172)
	s(config.d2_pin, 2500)
	goalTime = tt

def turnL(tt):
	global goalTime
	global state
	global startTime	
	state = 2
	startTime = time.time()
	s(config.d1_pin, 1771)
	s(config.d2_pin, 2500)
	goalTime = tt

def turnR(tt):
	global goalTime
	global state
	global startTime

	state = 2
	startTime = time.time()
	s(config.d1_pin, 700)
	s(config.d2_pin, 1000)
	goalTime = tt

def corr(tt):
	global goalTime
	global state
	global startTime
	state  = 3
	startTime = time.time()        
	s(config.d1_pin, 1172)
	s(config.d2_pin, 2500)
	goalTime = tt

def dn():
	global goalTime
	global state
	global t
	global started

	t = 0
	state = 0
	started = False
	stopAll()
	

def s(pin, state):
	pi.set_servo_pulsewidth(pin, state)

def stopAll():
	s(config.d1_pin, 1500)
	s(config.d2_pin, 1500)

ok = True
started = False
stopped = False

lastCamTime = time.time()
startTime = time.time()
state = 0 # 0 = none 1 = str 2 = turn 3 = correct


#stopAll()

while(ok):
	pressed = pi.read(config.b_pin) == 0
	if pressed:
		if not started:
			started = True
			t = 1
			#goStr(2)
			print("s1")
			turnR(1.41)
			print("s2")
	if time.time() - startTime > goalTime:
		if state == 1:
			# done going straight, start turning
			turnR(1.41)
			print("turning")

			# check to see if should stop
			t = t + 1
			if t == 2:
				# should stop here
				dn()
				print("ending")
		elif state == 2:
			# stop turning, start correcting
			corr(0.79)
			print("correcting")

		elif state == 3:
			dn()
			# stop correcting, start going straight
			#goStr(2)
			print("straight")
	


pi.stop()

def exit_handler():
	stopAll()
	print('My application is ending!')
	
atexit.register(exit_handler)
