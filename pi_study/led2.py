import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 20, 21)

#BCM	->	GPIO
#BOARD	->	BOARD
gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(ledPin, gpio.OUT)

try:
    isOnAll = False
    while True:
        for pin in ledPin:
            if isOnAll:
                gpio.output(pin, gpio.LOW)
            else:
                gpio.output(pin, gpio.HIGH)
            sleep(1)
        isOnAll = not isOnAll
finally:
    gpio.cleanup()
        
                        

        