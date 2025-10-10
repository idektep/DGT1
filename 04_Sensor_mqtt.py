import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
port = 1883
topic1 = "idt/temperature"
topic2 = "idt/humidity"

client = mqtt.Client()


temp = None
hum = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(topic1)
    client.subscribe(topic2)

def on_message(client, userdata, msg):
    global temp, hum

    topic = msg.topic
    try:
        value = float(msg.payload.decode())

        if topic == topic1:
            temp = value
            print(f"Temperature: {value}")
        elif topic == topic2:
            hum = value
            print(f"Humidity: {value}")


        if temp is not None and hum is not None:
            if temp > 27 :
                client.publish("traffic/N", "red")
            else:
                client.publish("traffic/N", "green")

    except ValueError:
        print("Error decoding payload")

client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)
client.loop_forever()
