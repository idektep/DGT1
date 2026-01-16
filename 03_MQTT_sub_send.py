import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
port = 1883
topic_temp = "temp_topic"
topic_led = "led_topic"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(topic_temp)

def on_message(client, userdata, msg):
    try:
        temp = float(msg.payload.decode())
        print(f"Temperature: {temp} °C")
    except ValueError:
        print("Error")
        
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)
client.loop_forever()

