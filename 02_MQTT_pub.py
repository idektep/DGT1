import paho.mqtt.client as mqtt
import time

broker = "broker.emqx.io"
client = mqtt.Client()
client.connect(broker, 1883)
client.publish("topic", "massage")




