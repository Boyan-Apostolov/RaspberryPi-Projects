
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1 = 18
led2 = 23
led3 = 24
button = 2

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

counter = 0

GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)
GPIO.output(led3, GPIO.LOW)

while True:
 if not GPIO.input(button):
  counter = counter + 1

 if counter == 1:
  GPIO.output(led1, GPIO.HIGH)
 elif counter == 2:
  GPIO.output(led2, GPIO.HIGH)
 elif counter == 3:
  GPIO.output(led3, GPIO.HIGH)
 else:
  counter = 0
  GPIO.output(led1, GPIO.LOW)
  GPIO.output(led2, GPIO.LOW)
  GPIO.output(led3, GPIO.LOW)

 time.sleep(0.5)

GPIO.cleanup()
