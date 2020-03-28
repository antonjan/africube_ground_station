import paho.mqtt.client as mqtt #import the client1
broker_address="iot.giga.co.za" 
client = mqtt.Client("africube_gateway") #create new instance
client.username_pw_set("africube","AE@m0squitt0")
client.connect(broker_address) #connect to broker
client.publish("africube/aprs","test123")#publish
