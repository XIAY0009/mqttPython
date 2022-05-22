import paho.mqtt.client as paho
import time
import struct
import binascii
from paho.mqtt import client as mqtt_client
import threading

topic = "response/topic"
client_id = "Yy"
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect("192.168.1.129", 1884)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global resetFlag
        global idxLine
        global pauseFlag
        global resumeFlag
        print ("hello, I'm subscribing")
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def subscribeThread(): 
    client2=connect_mqtt() 
    subscribe(client2) 
    client2.loop_forever() 

broker="10.42.0.199"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    #print("[] {} {}".format(userdata,result))
    pass

x = threading.Thread(target=subscribeThread)
x.start()


client1= paho.Client("emu")                         #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.connect(broker,port)                        #establish connection

idx=0
while 1:
    ret= client1.publish("hello/there", "My name is Yingyu")
    time.sleep(0.0667)


