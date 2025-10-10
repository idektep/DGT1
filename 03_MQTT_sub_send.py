import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
port = 1883
topic_temp = "idt/ldr"
topic_led = "idt/6/led1"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(topic_temp)

def on_message(client, userdata, msg):
    try:
        temp = float(msg.payload.decode())
        print(f"Temperature: {temp} °C")

        if temp > 3000:
            client.publish(topic_led, "on")
        else:
            client.publish(topic_led, "off")

    except ValueError:
        print("Error")
        
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)
client.loop_forever()
