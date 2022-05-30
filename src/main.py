'''
Description: 
Author: hecai
Date: 2022-04-26 17:44:03
LastEditTime: 2022-05-30 15:53:44
FilePath: \Lilygo-Wristband\src\main.py
'''
# 在这里写上你的代码 :-)
from machine import Pin,I2C
from machine import Timer
from display import Display
from max30102 import MAX30102
import json
import utime
import network
from umqttsimple import MQTTClient
from mpu9250 import MPU9250

lastClickTime = 0
pressTime = 0
pressTimer = Timer(1)
state = 0
initDisplay = False
lcd = Display()


mqtt_server = '192.168.0.20'
client_id="test"
topic_sub="lilygo/subinfo"
topic_pub="lilygo/pubinfo"
vibration = Pin(4, Pin.OUT)
# 触摸操作
# 给触摸芯片供电
touchPow = Pin(25, Pin.OUT)
touchPow.value(1)
# 绑定触摸按钮的中断事件
touch = Pin(33, Pin.IN)

# i2c =I2C(sda=Pin(15),scl=Pin(13),freq=100000)
i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU9250(i2c)
enableIrq=True

def do_connect():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    if not wifi.isconnected():
        print('connecting to network...')
        wifi.connect('MERCURY_032E', '5C88888C')   # 
        while not wifi.isconnected():
            pass
    print('network config:', wifi.ifconfig())

do_connect()


def click(pin):
    global state
    global touch
    global lastClickTime
    global pressTimer
    global enableIrq
    if not enableIrq:
        return
    if touch.value():
        state = 1
        pressTimer.init(period=1000, mode=Timer.ONE_SHOT, callback=longPress)
    else:
        clickTime = utime.ticks_ms()
        if state == 1:
            pressTimer.deinit() #关闭定时器
            if clickTime-lastClickTime < 400:
                doubleClick()
            else:
                lastClickTime = clickTime
                click()
touch.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=click)


def sub_cb(topic, msg):
  print((topic, msg))



def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server,1883,"siot","dfrobot")
  client.set_callback(sub_cb)
  client.connect()
  return client



def click():
    print("click")


def doubleClick():
    print("double click")
    global initDisplay
    global lcd
    global vibration
    global i2c
    global pressTimer
    global enableIrq
    if initDisplay:
        enableIrq=False
        for i in range(10):
            mqtt_client=connect_and_subscribe()
            tuple_str = json.dumps(sensor.acceleration)  
            mqtt_client.publish(topic_pub,tuple_str)
            lcd.PrintText(tuple_str)
            tuple_str = json.dumps(sensor.gyro)  
            mqtt_client.publish(topic_pub,tuple_str)
            lcd.PrintText(tuple_str)
            utime.sleep(1)
        lcd.clear()
        enableIrq=True

def longPress(t):
    print("long press")
    global initDisplay
    global lcd
    global state
    state=0
    if initDisplay==False:
        initDisplay=True
        lcd.init()
    else:
        lcd.clear()



