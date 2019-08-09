from tkinter import *
from PIL import ImageTk
from PIL import Image
import time
import threading
import pyttsx3
root=Tk()  #opens a window
root.title('MAIN') #title of gui
root.geometry('1000x1000')#specifies the size of window
frame=Frame(root,width=1100,height=1100)
frame.place(x=0,y=0)
img=PhotoImage(file='car parking.gif')
L1=Label(frame,image=img)
L1.image=img
L1.place(x=0,y=0)
def gofun(root,frame):
    frame.destroy()
    frame=Frame(root,width=1630,height=820)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('parking 3.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    L1=Label(frame,text='Charges',font=('Helvetica',80,'bold'),fg='red',bg='gray',width=22)
    L1.place(x=48,y=50)
    L2=Label(frame,text='Car Parking:',font=('arial',50,'bold'))
    L2.place(x=400,y=300)
    L3=Label(frame,text='Rs. 50',font=('arial',50,'bold'))
    L3.place(x=1000,y=400)
    L4=Label(frame,text='Bike Parking:',font=('arial',50,'bold'))
    L4.place(x=400,y=400)
    L5=Label(frame,text='Rs. 30',font=('arial',50,'bold'))
    L5.place(x=1000,y=300)
    B11=Button(root,text='Go...',font=('arial',30,'bold'),fg='red',bg='gray',bd=3)
    B11.place(x=1300,y=700)
    frame.mainloop()
def main(root):
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    L1=Label(frame,text='Parking Management System',font=('Helvetica',50,'bold'),fg='red',bg='gray')
    L1.place(x=10,y=100)     
    root.title('MAIN')
    B11=Button(root,text='Go...',font=('arial',30,'bold'),fg='red',bg='gray',bd=3,command=lambda : gofun(root,frame))
    B11.place(x=1300,y=700)
    frame.mainloop()
def speak(e,t):
    print('dfs')
    global t1,t2
    t=pyttsx3.init()
    rate=t.getProperty('rate')
    t.setProperty('rate',rate-25)
    t.say('welcome, to the parking services')
    t.runAndWait()
    print('fds')
    t.say('your venue is:')
    t.runAndWait()
    t.say('basement')
    t.runAndWait()
    t1=threading.Thread(target=dis,args=(e,1))
    t2=threading.Thread(target=speak,args=(e,1,))
    t1.start()
def dis(e,t):
    global frame,event,t1,t2 
    L1=Label(frame,text='Your venue is: Basement',font=('arial',30,'bold'),fg='red',bg='gray',width=30)
    L1.place(x=100,y=700)
    t1=threading.Thread(target=dis,args=(e,1))
    t2=threading.Thread(target=speak,args=(e,1,))
e=threading.Event()
t1=threading.Thread(target=dis,args=(e,1))
t2=threading.Thread(target=speak,args=(e,1,))
t2.start()
main(root)


