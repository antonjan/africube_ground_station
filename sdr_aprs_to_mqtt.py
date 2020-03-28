# APRS_to_MQTT.py
# A simple Python script by G7UHN to publish an MQTT message when
# given text is received by a RTL/BeagleBone APRS receiver
# pip3 install paho-mqtt

import sys
from subprocess import Popen, PIPE
import datetime
import paho.mqtt.client as mqtt #import the client1

broker_address="iot.giga.co.za"
client = mqtt.Client("africube_gateway") #create new instance
client.username_pw_set("africube","AE@m0squitt0")
client.connect(broker_address) #connect to broker
client.publish("africube/aprs","test123")#publish

//client = mqtt.Client("RTL-APR-VHF")
//client.connect("iot.giga.co.za")
//client.loop_start()

# General guidance from
# https://stackoverflow.com/questions/2804543/read-subprocess-stdout-line-by-line
# http://www.steves-internet-guide.com/into-mqtt-python-client/

proc = Popen('rtl_fm -p 50 -f 144.80M - | direwolf -c sdr.conf -r 24000 -t 0 -D 1 -', stdout=PIPE, shell=True)

while True:
    line = proc.stdout.readline()
    if line != '':
	#Open new data file
	aprs_str = line 
	f = open("aprs.txt", "a")
	f.write( str(aprs_str)  )      # str() converts to string
	f.close()
        client.publish("africube/aprs",aprs_str)#publish
        # Print each line received by Python to stdout
        print ("Decoded:", line.rstrip())

        # Look for a given text string...
        if "MQTT switch on" in line:
            # Send an MQTT message to the APRS topic
            #client.publish("APRS","Turn the switch on")
        if "MQTT switch off" in line:
            # Send an MQTT message to the APRS topic
            #client.publish("APRS","Turn the switch off")
    else: break

