# 在这里写上你的代码 :-)
from machine import Pin
def click(pin):
    if touch.value():
        print('%s keydown!' % (pin))
    else:
        print('%s keyup!' % (pin))

#给触摸芯片供电
touchPow = Pin(25, Pin.OUT)
touchPow.value(1)
#绑定触摸按钮的中断事件
touch = Pin(33, Pin.IN)
touch.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=click)
