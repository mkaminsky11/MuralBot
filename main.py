import time
import pigpio
import atexit
import config

import json

import json
from pprint import pprint

data = []
have = []
rows = 0
cols = 0

with open('data.json') as data_file:    
	d = json.load(data_file)
	data = d["data"]
	have = d["have"]
	rows = len(data)
	cols = len(data[0])

pi = pigpio.pi()
if not pi.connected:
	print("exit")
	exit()
# all good, keep going

turns = 0
t = 0
goalTime = 0
row = 0
col = 0

timeToRow = 24 / (29.5 / 4)

def getCol():
	global startTime
	time_elap = time.time() - startTime
	dist_traveled = (29.5 / 4) * time_elap
	c = int((dist_traveled - (dist_traveled % 0.75)) / 0.75)
	if c > (cols - 1):
		c = cols - 1
	if c < 0:
		c = 0
	return c

def goStr(tt):
	global goalTime
	global state
	global startTime
	state = 1
	startTime = time.time()
	s(config.d1_pin, 1132)
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
	s(config.d2_pin, 1200)
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
	global have
	global turns

	t = 0
	state = 0
	started = False
	row = 0
	col = 0
	turns = 0
	have = []
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

stopAll()

while(ok):
	pressed = pi.read(config.b_pin) == 0
	if pressed:
		if not started:
			started = True
			t = 1
			goStr(2)
			print("s1")
			#turnR(1.17) # remove this and stuff
			print("s2")
	if time.time() - startTime > goalTime:
		if state == 1:
			# done going straight, start turning
			if turns % 2 == 0:	
				turnR(1.37)
			else:
				turnL(1.30)
			turns = turns + 1
			row = row + 1
			print("turning")

			# check to see if should stop
			# REMOVE THIS
			t = t + 1
			if t == rows:
				# should stop here
				dn()
				print("ending")
		elif state == 2:
			# stop turning, start correcting
			corr(0.79)
			print("correcting")

		elif state == 3:
			#dn()
			# stop correcting, start going straight
			goStr(2)
			print("straight")

	if state == 1 and data[row][getCol()] == True and have[row][getCol()] == False:
		# spray some stuff here
		print(row, getCol())
		pi.set_servo_pulsewidth(12, 800)
		time.sleep(0.3)
		pi.set_servo_pulsewidth(12, 1500)


pi.stop()

def exit_handler():
	stopAll()
	print('My application is ending!')
	
atexit.register(exit_handler)
