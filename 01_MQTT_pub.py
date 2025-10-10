import paho.mqtt.client as mqtt
import time

broker = "_______________"
client = mqtt.Client()
client.connect(broker, 1883)

while True:
    client.publish("topic", 22.4)
    time.sleep(1)


