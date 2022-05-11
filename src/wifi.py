# wifi功能
import network
wifi = network.WLAN(network.STA_IF) # 创建一个Wifi站点
wifi.active(True)       # 激活该站点
wifi.connect('ssid', 'password')   # 