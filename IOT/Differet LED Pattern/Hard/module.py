# For Blinking
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,OUT)
GPIO.setup(5,OUT)
GPIO.setup(7,OUT)
while True:
    GPIO.output(3,True)
    time.sleep(2)
    GPIO.output(3,False)
    GPIO.output(5,True)
    time.sleep(2)
    GPIO.output(5,False)
    time.sleep(2)
    GPIO.output(7,False)