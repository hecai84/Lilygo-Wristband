'''
Description: 
Author: hecai
Date: 2022-04-26 17:44:03
LastEditTime: 2022-05-14 22:34:09
FilePath: \Lilygo-Wristband\src\main.py
'''
# 在这里写上你的代码 :-)
from machine import Pin,I2C
from machine import Timer
from display import Display
from max30102 import MAX30102
import json
import utime

lastClickTime = 0
pressTime = 0
pressTimer = Timer(1)
state = 0
initDisplay = False
lcd = Display()

vibration = Pin(4, Pin.OUT)
# 触摸操作
# 给触摸芯片供电
touchPow = Pin(25, Pin.OUT)
touchPow.value(1)
# 绑定触摸按钮的中断事件
touch = Pin(33, Pin.IN)

i2c =I2C(sda=Pin(15),scl=Pin(13),freq=100000)
enableIrq=True

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
        lcd.PrintText(json.dumps(i2c.scan()))
        if len(i2c.scan())>0:
            lcd.PrintText("init 30102")
            sensor = MAX30102(i2cHexAddress = 0x57, i2c = i2c)
            sensor.setup_sensor()s
            sensor.set_sample_rate(800)
            sensor.set_fifo_average(8)
            lcd.PrintText("setup 30102")
            utime.sleep(1)
            sensor.startCheck(60000,lcd)
            # del sensor
        else:
            lcd.PrintText("not found 30102")
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



