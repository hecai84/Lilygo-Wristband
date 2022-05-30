'''
Description: 
Author: hecai
Date: 2022-05-30 15:11:41
LastEditTime: 2022-05-30 15:41:53
FilePath: \Lilygo-Wristband\src\mqtt.py
'''
# wifi功能
import network
from umqttsimple import MQTTClient
import ubinascii
import utime

mqtt_server = '192.168.0.20'
client_id="test"
topic_sub="lilygo/subinfo"
topic_pub="lilygo/pubinfo"

def sub_cb(topic, msg):
  print((topic, msg))

def do_connect():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    if not wifi.isconnected():
        print('connecting to network...')
        wifi.connect('MERCURY_032E', '5C88888C')   # 
        while not wifi.isconnected():
            pass
    print('network config:', wifi.ifconfig())

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server,1883,"siot","dfrobot")
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

do_connect()
mqtt_client=connect_and_subscribe()
while True:
    mqtt_client.publish(topic_pub,"info")
    utime.sleep(5)