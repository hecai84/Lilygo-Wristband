# 按键处理程序
# 通过中断的方式,获取按键的动作
from machine import Pin
def click(pin):
    global touch
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
