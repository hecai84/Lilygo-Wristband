'''
Description:
Author: hecai
Date: 2022-04-26 16:59:36
LastEditTime: 2022-05-11 18:01:49
FilePath: \Lilygo-Wristband\src\display.py
'''
from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin

class Display:
    # spi = SPI(2, baudr2ate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(12))
    spi=...
    tft=...
    posY=0
    def __init__(self):
        ...
    def init(self):
        self.spi = SPI(2,baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
        self.tft=TFT(self.spi,23,26,5,blk=27)
        self.tft.initr()
        self.tft.rgb(True)
        self.tft.fill(TFT.BLACK)   

    def clear(self):
        self.tft.fill(TFT.BLACK)
        self.posY=0


    def PrintText(self,text,color:int=TFT.WHITE):
        if self.posY==160:
            self.clear()
        self.tft.text((0, self.posY), text, color, sysfont, 1)
        self.posY += sysfont["Height"]

