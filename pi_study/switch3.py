import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

class Led:
    def _init_(self, pin, color):
        self.pin = pin
        self.color = color
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin,gpio.LOW)
        
    def blink(self, count):
        for _ in range(count):
            gpio.output(self.pin,gpio.HIGH)
            slepp(time)
            gpio.output(self.pin,gpio.LOW)
            slepp(time)
            
    def ledOn(self):
        gpio.output(self.pin, gpio.HIGH)
        
    def ledOff(self):
        gpio.output(self.pin, gpio.LOW)

class Button:
    
    def __init__(self, pin, onPressed):
        self.pin = pin
        self.prevState = gpio.LOW
        self.onPressed = onPressed
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        
    def waitPressed(self):
        currentState = gpio.input(self.pin)
        if self.checkPressed(currentState):
            self.onPressed()
        self.prevState = currentState
        sleep(0.05)
        
    def checkPressed(self, currentState):
        return currentState == gpio.HIGH and self.prevState == gpio.LOW

def open():
    print("open door")
    
def close():
    print("close door")

buttons = (Button(13, open), Button(19, close))
    
try:
    while True:
        for button in buttons:
            button.waitPressed()
        
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()