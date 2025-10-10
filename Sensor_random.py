import paho.mqtt.client as mqtt
import time
import random

broker = "broker.emqx.io"
client = mqtt.Client()
client.connect(broker, 1883)

while True:
    temperature = round(random.uniform(25.0, 30.0), 1)      # °C
    humidity = round(random.uniform(40.0, 60.0), 1)         # %
    pressure = round(random.uniform(1000.0, 1020.0), 1)     # hPa
    gas = round(random.uniform(300.0, 600.0), 1)            # ppm
    light = round(random.uniform(100.0, 800.0), 0)          # lux
    altitude = round(random.uniform(10.0, 50.0), 2)         # meters

    client.publish("idt/temperature", str(temperature))
    client.publish("idt/humidity", str(humidity))
    client.publish("idt/pressure", str(pressure))
    client.publish("idt/gas", str(gas))
    client.publish("idt/light", str(light))
    client.publish("idt/altitude", str(altitude))

    print(f"Sent: Temp={temperature}°C | Hum={humidity}% | Pressure={pressure}hPa | Gas={gas}ppm | Light={light}lux | Alt={altitude}m")
    time.sleep(2)
