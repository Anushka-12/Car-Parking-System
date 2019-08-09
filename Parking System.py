import RPi.GPIO as GPIO
from time import sleep
import random
import urllib.request
#import requests
import threading
#import urllib.urlopen


IR1 = 2
IR2 = 3
IR3 = 4
IR4 = 14

IR_I1 = 15
IR_I2 = 16
IR_E1 = 17
IR_E2 = 27

Ser1 = 22
Ser2 = 23

V1 = 24
V2 = 10
V3 = 9
V4 = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(IR1,GPIO.IN)
GPIO.setup(IR2,GPIO.IN)
GPIO.setup(IR3,GPIO.IN)
GPIO.setup(IR4,GPIO.IN)

GPIO.setup(IR_I1,GPIO.IN)
GPIO.setup(IR_I2,GPIO.IN)
GPIO.setup(IR_E1,GPIO.IN)
GPIO.setup(IR_E2,GPIO.IN)

GPIO.setup(Ser1,GPIO.OUT)
GPIO.setup(Ser2,GPIO.OUT)

GPIO.setup(V1,GPIO.OUT)
GPIO.setup(V2,GPIO.OUT)
GPIO.setup(V3,GPIO.OUT)
GPIO.setup(V4,GPIO.OUT)

def thingspeak_post(x,y,z,w):
    #threading.Timer(15,thingspeak_post).start()
    URL='https://api.thingspeak.com/update?api_key='
    KEY='PVI91ALIJ1TNIYHN'
    HEADER='&field1={}&feild2={}&feild3={}&feild4={}'.format(x,y,z,w)
    Full_URL=URL+KEY+HEADER
    print(Full_URL)
    data=urllib.request.urlopen(Full_URL)
    print(data)

def SetAngle(Servo,angle):
    duty=angle/18 + 2
    GPIO.output(Servo,True)
    p=GPIO.PWM(Servo,50)
    p.start(0)

    p.ChangeDutyCycle(duty)
    sleep(2)
    p.stop()
'''
SetAngle(Ser1,10)
sleep(2)
SetAngle(Ser2,10)
sleep(2)'''

while True:
    slot1 = GPIO.input(IR1)
    slot2 = GPIO.input(IR2)
    slot3 = GPIO.input(IR3)
    slot4 = GPIO.input(IR4)
    thingspeak_post(slot1,slot2,slot3,slot4)
    Entry1 = GPIO.input(IR_I1)
    e=GPIO.input(IR_I2)
    Exit1 = GPIO.input(IR_E1)
    #print(Exit1)
    if(slot1==1 or slot2==1 or slot3==1 or slot4==1):
        if Entry1 ==0:
            print('Vehicle come for parking.')
            SetAngle(Ser1,50)
            if(GPIO.input(IR_I2)==0): 
               SetAngle(Ser1,0) 
                
    
    if Exit1 ==1:
        print('Vehicle is about to exit.')
        SetAngle(Ser2,50)
        print(GPIO.input(IR_E2))
        if(GPIO.input(IR_E2)==0): 
            print(1)    
            SetAngle(Ser2,0) 
        
