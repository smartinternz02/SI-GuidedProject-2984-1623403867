import wiotp.sdk.device
import time
import os
import datetime
import random
myConfig = {
     "identity": {
	 "orgId": "g3y4kb",
	 "typeId": "iotdevice",
	 "deviceId":"1001"
     },
     "auth": {
	 "token":"1234567890"
     }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="lighton"):
        print("Light is swithched ON")
    elif(m=="lightoff"):
        print("Light is swithched OFF")
    elif(m=="fanon"):
        print("Fan is swithched ON")
    elif(m=="fanoff"):
        print("Fan is swithched OFF")
    print(" ")
client = wiotp.sdk.device.DeviceClient(config = myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    myData={'temperature':temp, 'humidity':hum}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
	    
