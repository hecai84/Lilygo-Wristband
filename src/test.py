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
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

    utime.sleep_ms(1000)
