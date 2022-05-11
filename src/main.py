# 在这里写上你的代码 :-)
from machine import Pin,I2C
from machine import Timer
from display import Display
import utime

lastClickTime=0
pressTime=0
pressTimer = Timer(1)
state=0
initDisplay = False
lcd=Display()
# 触摸操作
#给触摸芯片供电
touchPow = Pin(25, Pin.OUT)
touchPow.value(1)
#绑定触摸按钮的中断事件
touch = Pin(33, Pin.IN)
def click(pin):
    global state
    global touch
    global lastClickTime
    global pressTimer
    if touch.value():
        state=1
        pressTimer.init(period=1000, mode=Timer.ONE_SHOT, callback=longPress)
    else:
        clickTime=utime.ticks_ms()
        if state==1:
            if clickTime-lastClickTime<400:
                doubleClick()
            else:
                lastClickTime=clickTime
                click()
        pressTimer.deinit()
touch.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=click)



def click():
    print("click")
    global state
    global initDisplay
    global lcd
    state=0
    if initDisplay:
        lcd.PrintText("click")

def doubleClick():
    print("double click")
    global state
    global initDisplay
    global lcd
    global sensor
    state=0
    if initDisplay:   
        lcd.PrintText("doubleClick")     
        

def longPress(t):
    print("long press")
    global state
    global initDisplay
    global lcd
    state=0
    if initDisplay==False:
        initDisplay=True
        lcd.init()
    else:
        lcd.clear()



