import utime
from machine import I2C, Pin
from mpu9250 import MPU9250

i2c = I2C(scl=Pin(22), sda=Pin(21))
print("1")
print(i2c.scan()) # this displays [39]
print("2")
sensor = MPU9250(i2c)
print("3")

while True:
    print(sensor.acceleration) #加速度  x,y,z
    print(sensor.gyro) # 旋转角度 x,y,z deg/s
    print(sensor.magnetic)  # 地磁
    print(sensor.temperature) # 温度

    utime.sleep_ms(1000)