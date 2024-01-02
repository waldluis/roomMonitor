import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = ""
org = "admin"
url = "http://192.168.178.200:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="test"


write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("mem").tag("host", "host1").field("temperature", 23.43).field("humidity", 10.0)
write_api.write(bucket=bucket, org=org, record=p)

# for value in range(5):
#   point = (
#     Point("measurement1")
#     .tag("tagname1", "tagvalue1")
#     .field("field1", value)
#   )
#   write_api.write(bucket=bucket, org="admin", record=point)
#   time.sleep(1) # separate points by 1 second
