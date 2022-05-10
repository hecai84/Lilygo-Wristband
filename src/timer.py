#定时器相关功能
import utime
from machine import Timer

print(utime.time())
print(utime.ticks_ms())

# 使用延时做定时
count=0
while count<5:
    print(count)
    utime.sleep_ms(1000)
    count+=1

# 使用定时器做定时 
count=0
timer = Timer(1)
# 注意:在定时器的回调函数里面,最好不要print,不然调试可能会出现不可预期的错误
def test(t):
    global count
    global timer
    count+=1
    print(count)
    if count>=5:
      timer.deinit()
timer.init(period=1000, mode=Timer.PERIODIC, callback=test)

