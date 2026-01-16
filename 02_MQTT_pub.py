import paho.mqtt.client as mqtt
import time

broker = "broker.emqx.io"
client = mqtt.Client()
client.connect(broker, 1883)

while True:
    
    client.publish("idt/4/led1", "on")
    client.publish("idt/4/led2", "on")
    client.publish("idt/4/led3", "on")
    client.publish("idt/4/led4", "on")
    client.publish("idt/4/led5", "on")
    client.publish("idt/4/led6", "on")
    time.sleep(1)
    client.publish("idt/4/led1", "off")
    client.publish("idt/4/led2", "off")
    client.publish("idt/4/led3", "off")
    client.publish("idt/4/led4", "off")
    client.publish("idt/4/led5", "off")
    client.publish("idt/4/led6", "off")
    time.sleep(1)


