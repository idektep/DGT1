import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# ----------- InfluxDB Setup -----------
url = "http://localhost:8086"
token = ""
org = ""
bucket = ""

influx_client = InfluxDBClient(url=url, token=token, org=org)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

# ----------- MQTT Callback -----------
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT with result code", rc)
    client.subscribe("idt/temperature")

def on_message(client, userdata, msg):
    try:
        payload = float(msg.payload.decode())  # สมมุติว่าได้ค่า temp ตรงๆ เช่น 25.6
        print(f"Received temp: {payload}")

        point = Point("temperature").tag("room", "lab1").field("value", payload)
        write_api.write(bucket=bucket, org=org, record=point)

        print("Written to InfluxDB.")
    except Exception as e:
        print("Error:", e)

# ----------- MQTT Setup -----------
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_broker = "broker.emqx.io"  # หรือใช้ IP/localhost ตาม setup จริง
mqtt_port = 1883

mqtt_client.connect(mqtt_broker, mqtt_port, 60)
mqtt_client.loop_forever()
