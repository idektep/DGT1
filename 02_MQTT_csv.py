import csv
import time
from datetime import datetime
import paho.mqtt.client as mqtt

filename = "______________.csv"
fieldnames = ["timestamp", "value"]

counter = 0
max_count = _____


with open(filename, "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()


def on_message(client, userdata, msg):
    global counter
    if counter >= max_count:
        return
    try:
        value = float(msg.payload.decode())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({"timestamp": timestamp, "value": value})

        print(f"[{timestamp}] value: {value}")
        counter += 1
    except Exception as e:
        print("Error:", e)


broker = "____________"
port = 1883
topic = "_________________"
client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port)
client.subscribe(topic)
client.loop_start()

while counter < max_count:
    time.sleep(2)
client.loop_stop()
client.disconnect()
print("Done. Data saved to:", filename)


