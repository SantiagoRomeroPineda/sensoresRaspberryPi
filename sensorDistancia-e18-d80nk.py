import RPi.GPIO as GPIO
import time
import sys
import os 
from subprocess import Popen


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ECHO1 = 17
ECHO2 = 18
ECHO3 = 15
movie= "/home/pi/Videos/club.mp4"
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(ECHO3,GPIO.IN)
while 1:
	if not GPIO.input(ECHO1) and not GPIO.input(ECHO2) :
		print("far")
	
	if  (GPIO.input(ECHO1) and   GPIO.input(ECHO2)) or GPIO.input(ECHO3) :
		os.system('killall omxplayer.bin')
		omxc = Popen(['omxplayer', '-b', movie])
		os.system('killall omxplayer.bin')
		print("near")
		time.sleep(31)
		
		
	
        
