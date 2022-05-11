# 复杂的按键处理程序,处理双击,长按动作
# 通过判断两次按键的时间,判断双击动作
# 通过定时器,判断长按动作
from machine import Pin
from machine import Timer
import utime

lastClickTime=0
pressTime=0
# 定义定时器
pressTimer = Timer(1)
# 按键状态,按下为1,用于处理长按操作之后忽略掉单击操作
state=0
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
        pressTimer.init(period=2000, mode=Timer.ONE_SHOT, callback=longPress)
    else:
        clickTime=utime.ticks_ms()
        if state==1:
            if clickTime-lastClickTime<800:
                doubleClick()
            else:
                lastClickTime=clickTime
                click()
        pressTimer.deinit()
touch.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=click)


# 单击
def click():
    print("click")
    global state
    state=0
# 双击
def doubleClick():
    print("double click")
    global state
    state=0
# 长按
def longPress(t):
    print("long press")
    global state
    state=0




