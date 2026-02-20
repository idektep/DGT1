from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = "http://localhost:8086"
token = ""
org = ""
bucket = ""

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# --- Create Points ---
point1 = Point("temperature").tag("room", "lab1").field("value", 25.0)
point2 = Point("humidity").tag("room", "lab1").field("value", 60.0)

# --- Write Multiple Points ---
write_api.write(bucket=bucket, org=org, record=[point1, point2])

print("Sent 2 data points!")
