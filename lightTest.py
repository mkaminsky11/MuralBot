#import sys
import time
#import random
import pigpio
#import atexit

green_gpio = 19

pi = pigpio.pi()


#pi.write(red_gpio,0)
pi.write(green_gpio,1)
time.sleep(2)
#pi.write(red_gpio,1)
pi.write(green_gpio,0)
pi.stop()
