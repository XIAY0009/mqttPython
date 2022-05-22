import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
 
Connected = False   #global variable for the state of the connection
 
broker_address= "192.168.1.129"
port = 1884
 
client = mqttClient.Client("Python")               #create new instance
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
while Connected != True:    #Wait for connection
    time.sleep(0.1)
try:
    while True:
        value = "hellp"
        client.publish("response/topic",value)
 
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
