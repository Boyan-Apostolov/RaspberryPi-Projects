import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) 	#LED on gpio18

GPIO.output(18, GPIO.HIGH) 	#5v

time.sleep(3) 			#delay 3s

GPIO.output(18, GPIO.LOW)	 #0v
GPIO.cleanup() 			#clear gpio
