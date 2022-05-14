
from machine import I2C, Pin
from max30102 import MAX30102
import json

# Alternative:
i2c = I2C(sda=Pin(15),scl=Pin(13),freq=100000)
sensor = MAX30102(i2cHexAddress = 0x57, i2c = i2c)

print(json.dumps())
