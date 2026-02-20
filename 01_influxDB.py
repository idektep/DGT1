from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = "http://localhost:8086"
token = ""
org = ""
bucket = ""

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)


point = Point("temperature").tag("room", "lab1").field("value", 200.2)
write_api.write(bucket=bucket, org=org, record=point)

print("Sent!")



