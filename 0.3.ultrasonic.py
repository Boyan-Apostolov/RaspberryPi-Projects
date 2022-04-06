import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pinout
led1 = 18
led2 = 23
led3 = 24
trig = 20
echo = 21

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def measure():

# Activate Ultrasonic sensor
 GPIO.output(trig, False)
 time.sleep(1)

 GPIO.output(trig, True)
 time.sleep(0.00001)
 GPIO.output(trig, False)

# Measure distance
 while GPIO.input(echo) == 0:
  pulse_start = time.time()

 while GPIO.input(echo) == 1:
  pulse_end = time.time()

# Calculate the distance
 pulse_duration = pulse_end - pulse_start

# Speed of sound at sea level baseline - 343m/s -> cm/s -> ÷2
 distance = pulse_duration * 17150

 distance = round(distance, 2)

 return distance

while True:
 dist = measure()
 print(dist)

 if dist < 15:
  GPIO.output(led1, GPIO.HIGH)
  GPIO.output(led2, GPIO.HIGH)
  GPIO.output(led3, GPIO.HIGH)
 elif dist > 15 and dist < 25:
  GPIO.output(led1, GPIO.HIGH)
  GPIO.output(led2, GPIO.HIGH)
  GPIO.output(led3, GPIO.LOW)
 elif dist > 25 and dist < 100:
  GPIO.output(led1, GPIO.HIGH)
  GPIO.output(led2, GPIO.LOW)
  GPIO.output(led3, GPIO.LOW)
 elif dist > 100:
  GPIO.output(led1, GPIO.LOW)
  GPIO.output(led2, GPIO.LOW)
  GPIO.output(led3, GPIO.LOW)

GPIO.cleanup()
