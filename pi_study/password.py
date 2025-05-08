import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 21)

gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(ledPin, gpio.OUT)

currntPassword = None

while True:
    newpassword = int(input("new password : "))
    confirmpassword = int(input("confirm password : "))
        
    if newpassword == confirmpassword:
        currntPassword = newpassword
        print("password OK")
        break    
    else:
        print("password NO")
        
while True:
    loginpassword = int(input("login password : "))
    if newpassword == loginpassword:
        gpio.output(ledPin[1], gpio.HIGH)
        break
    else:
        for i in range(5):
            gpio.output(ledPin[0], gpio.HIGH)
            sleep(0,5)
            gpio.output(ledPin[0], gpio.LOW)
            sleep(0.5)
            



            
        
        

