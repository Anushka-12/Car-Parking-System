import random
import urllib.request
import requests
import threading
#import urllib.urlopen
from bs4 import BeautifulSoup

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val=random.randint(1,30)
    val2=val*1.2
    URL='https://api.thingspeak.com/update?api_key='
    KEY='E35KZD459RX9IANZ'
    HEADER='&field1={}'.format(val)
    Full_URL=URL+KEY+HEADER
    print(Full_URL)
    data=urllib.request.urlopen(Full_URL)
    print(data)

thingspeak_post()

