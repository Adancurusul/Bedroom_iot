from umqtt.simple import MQTTClient
from machine import Pin,Timer
import network
import time
import random
#SSID = 'kali'
#PASSWORD='adaM3131'
SSID='adan'
PASSWORD='313115249'
door=Pin(2, Pin.OUT, value=0)
SERVER='adancurusul.picp.net'
CLIENT_ID='whatever'
TOPIC=b'opendoor'
TOPIC_R= b'state'
TOPIC2=b'key'
username='123123'
password='321321'
sta = 0
check_p = 0
state=0
c=None
tim = Timer(4)


def check(t):
    global sta,check_p
    if sta<60:
        sta+=1
        #print(sta)
    else :
        sta=0
        check_p =1




tim.init(freq = 1, callback=check)
def sub_cb(topic, msg):

    global state,key_of_door
    print((topic, msg))
    msg = str(msg)
    key_now = "b'"+key_of_door+"'"


    if msg ==key_now:
            door.value(1)
            #c.publish(TOPIC2,'on',retain=True)
            print("on")
            time.sleep(1)
            door.value(0)


    else:
        print(msg)
        state = 1
def connectWifi(ssid,passwd):
    global wlan
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(ssid,passwd)
    while(wlan.ifconfig()[0]=='0.0.0.0'):
        time.sleep(1)
try:
    connectWifi(SSID,PASSWORD)
    server=SERVER
    c=MQTTClient(CLIENT_ID, server,0,username,password)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    key_of_door =str(random.randint(10000,99999))
    c.publish(TOPIC2,key_of_door,retain=True)
    print('Connected to %s, subscribed to %s topic' % (server, TOPIC))
    while True:
        if check_p ==1:
            check_p =0

            key_of_door_r = str(random.randint(1,99999))
            m = 5-len(key_of_door)
            key_of_door = '0'*m+key_of_door_r
            print (key_of_door)
            c.publish(TOPIC2,key_of_door,retain=True)
        elif state ==1:
            c.publish(TOPIC_R,"wrong password",retain=True)
            state=0



        c.wait_msg()
finally:
    if(c is not None):
        c.disconnect()
    wlan.disconnect()
    wlan.active(False)