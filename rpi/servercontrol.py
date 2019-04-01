import socket            
import RPi.GPIO as GPIO
from time import sleep

#setting up the pins for first motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

#setting up the pins for second motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

#setting up the pulse width modulation for first motor
pwm=GPIO.PWM(7,100)
pwm.start(0)

#setting up the pulse width modulation for second motor
pwm=GPIO.PWM(36,100)


#thrust function
def thrust():
    pwm.ChangeDutyCycle(75)
    GPIO.output(3,True)
    GPIO.output(5,False)
    GPIO.output(7,True)         #Enabling Enable pin for first motor
    GPIO.output(38,True)
    GPIO.output(40,False)
    GPIO.output(36,True)        #Enabling Enable pin for second motor
    sleep(1)
    GPIO.output(7,False)        #disabling Enable pin for first motor
    GPIO.output(36,False)       #disabling Enable pin for second motor

#reverse function
def reverse():
    pwm.ChangeDutyCycle(75)
    GPIO.output(3,False)
    GPIO.output(5,True)
    GPIO.output(7,True)         #Enabling Enable pin for first motor
    GPIO.output(38,False)
    GPIO.output(40,True)
    GPIO.output(36,True)        #Enabling Enable pin for second motor
    sleep(1)
    GPIO.output(7,False)        #disabling Enable pin for first motor
    GPIO.output(36,False)       #disabling Enable pin for second motor

def left():
    pwm.ChangeDutyCycle(75)
    GPIO.output(3,False)
    GPIO.output(5,True)
    GPIO.output(7,True) 
    GPIO.output(38,True)
    GPIO.output(40,False)
    GPIO.output(36,True) 
    sleep(1)
    GPIO.output(7,False)        #disabling Enable pin for first motor
    GPIO.output(36,False)

def right():
    pwm.ChangeDutyCycle(75)
    GPIO.output(3,True)
    GPIO.output(5,False)
    GPIO.output(7,True) 
    GPIO.output(38,False)
    GPIO.output(40,True)
    GPIO.output(36,True)
    sleep(1)
    GPIO.output(7,False)        #disabling Enable pin for first motor
    GPIO.output(36,False)

s = socket.socket()      

 
port = 9999             
 
s.connect(('192.168.43.147', port)) 

while True:
    control=str(s.recv(1024))

    if control=="left":
        left()
    elif control=="right":
        right()
    elif control=="thrust":
        thrust()
    elif control=="reverse":
        reverse()

s.close()    

