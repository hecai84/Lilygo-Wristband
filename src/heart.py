# 心率检测程序

from machine import Pin,I2C
from max30102 import MAX30102
import utime

i2c =I2C(sda=Pin(15),scl=Pin(13),freq=100000)
sensor = MAX30102(i2cHexAddress = 0x57, i2c = i2c)
sensor.setup_sensor()
sensor.set_sample_rate(800)
sensor.set_fifo_average(8)
print("setup 30102")
utime.sleep(1)
print(sensor.startCheck(60000,None))
