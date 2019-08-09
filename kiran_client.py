import random
import urllib.request
import requests
import threading
from bs4 import BeautifulSoup
import re

def multi_re_find(patterns,phrase):
    for pat in patterns:
        return re.findall(pat,phrase)
        
def read_data():
    global f
    threading.Timer(10,read_data).start()
    data=urllib.request.urlopen('https://api.thingspeak.com/channels/811156/fields/1.json?api_key=OGAQKAI7NXKSI0ZZ&results=2')
    sel=data.read()
    #print(sel)
    sel=sel.decode('utf-8')
    #print(type(sel))
    #print(sel)
    status = multi_re_find([r'"field1":"[0-9]+'],sel)
    #print(status)
    previous_status = status[0].split(':"')
    current_status = status[1].split(':"')
    print('Previous Status is: ',previous_status[1])
    print('Current Status is: ',current_status[1])
    print()
    '''if current_status[1]=='100':
        print('Device On')
    elif current_status[1]=='0':
        print('Device Off')
    val=random.randint(1,30)
    val2=val*1.2
    URL='https://api.thingspeak.com/update?api_key='
    KEY='GTNBWPC19WJBOCOJ'
    HEADER='&field1={}&field2={}'.format(val,val2)
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)'''
read_data()
