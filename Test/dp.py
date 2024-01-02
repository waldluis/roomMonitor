import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "admin"
url = "http://192.168.178.200:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
