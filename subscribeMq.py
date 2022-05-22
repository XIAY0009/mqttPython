import paho.mqtt.client as mqtt #import the client1
import time

def on_message(client,userdata,msg) :
    topic=msg.topic
    mq_data=msg.payload
    print ("mq_data:  ", mq_data)

def on_connect(client, userdata, flags, rc) :
     if rc==0:
         print("connected ok")
     else:
         print("not connected", rc)

def on_disconnect(client, userdata, flags, rc=0) :
    print("disconnect result code "+str(rc))

def on_log(client, userdata, level, buf) :
    #print("log: "+buf)
    k=0


#LL Emulator
broker_address_rec="10.42.0.199"
#Wilson address
broker_address_pub="192.168.1.129"
#LL Emulator
port_rec=1883
#Wilson address
port_pub=1884

#MQTT
client = mqtt.Client("P2") #create new instance
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_log=on_log
client.on_message=on_message

client.connect(broker_address_rec, port_rec, 60)
#client.subscribe("irisys/V4D-20300894/0021AC041816/targets2")
client.subscribe("hello/there")


client.loop_forever()

