import RPi.GPIO as GPIO
from time import sleep
#Slot IR sensor
IR1=2
IR2=3
IR3=4
IR4=14

#Entry and exit gate sensor IR
IR_I1=15
IR_I2=16
IR_E1=17
IR_E2=27

#Servo motor
Ser1=22
Ser2=23


#Display LED(Entry)
V1=24
V2=10
V3=9
V4=11

GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)


#Pin setup(Input\output)
GPIO.setup(IR1,GPIO.IN)
GPIO.setuo(IR2,GPIO.IN)
GPIO.setup(IR3,GPIO.IN)
GPIO.setup(IR4,GPIO.IN)

GPIO.setup(IR_I1,GPIO.IN)
GPIO.setup(IR_I2,GPIO.IN)
GPIO.setup(IR_E1,GPIO.IN)
GPIO.setup(IR_E1,GPIO.IN)

GPIO.setup(Ser1,GPIO.OUT)
GPIO.setup(Ser2,GPIO.OUT)

GPIO.setup(V1,GPIO.OUT)
GPIO.setup(V2,GPIO.OUT)
GPIO.setup(V3,GPIO.OUT)
GPIO.setup(V4,GPIO.OUT)




#Angle Set of servo motor

def SetAngle(Servo,angle):
    duty=angle/18+2
    GPIO.OUT(Servo,True)
    p=GPIO.PWM(Servo,50)
    p.start(0)

    p.ChangeDutyCycle(duty)
    sleep(2)
    p.stop()

SetAngle(Ser1,10)
sleep(2)
SetAngle(Ser2,10)
sleep(2)

while True:
    slot1=GPIO.input(IR1)
    slot2=GPIO.input(IR2)
    slot3=GPIO.input(IR3)
    slot4=GPIO.input(IR4)

    Entry1=GPIO.input(IR_I1)
    Exit1=GPIO.input(IR_E1)

    if(slot1==1 or slot2==1 or slot3==1 or slot4==1):
     if(Entry1==0):
         print("Vehicle come for parking")
         SetAngle(SEr1,90)
         while(GPIO.input(IR_I2)==1):
             continue
         sleep(1)
         SetAngle(Ser1,10)
    if (Exit1==0):
        print("Vehicle about to exit")
        SetAngle(Ser2,90)
        while(GPIO.input(IR_E2==1)):
            continue
        sleep(1)
        SetAngle(Ser2,10)
         

