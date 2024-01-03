from paho.mqtt import client as mqtt_client
import datetime
import json
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# region Global variables
broker = '192.168.178.200'
port = 1883
topic = "roomMonitor/PicoWDHT22"
client_id = 'RaspiDataMonitor'

# endregion


def connect_mqtt() -> mqtt_client:
    """
    Connects to the MQTT Broker and returns the MQTT client object.

    Returns:
        mqtt_client: The MQTT client object.
    """
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def on_message(client, userdata, msg):
    """
    Callback function that is called when a message is received. Writes received data to file with timestamp.

    Args:
        client: The MQTT client instance.
        userdata: The user data passed to the MQTT client.
        msg: The received message object.

    Returns:
        None
    """
    # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    str_in = str(msg.payload.decode("UTF-8"))
    data_in = json.loads(str_in)

    data = {
        "Temperature": data_in['temperature'],
        "Humidity": data_in['humidity'],
    }

    # Write to InfluxDB
    token = "fzrKNIgdcLi4Ed65EnPoSmL-CWH1KG9YqBOhlCEAqmg0NU9ibVtb-2g5MUnREoi8huL0Y2f8-3Shgi45wN5Yhg=="
    org = "admin"
    url = "http://192.168.178.200:8086"
    bucket = "roomMonitor"

    clientDatabase = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    write_api = clientDatabase.write_api(write_options=SYNCHRONOUS)
    dataWrite = influxdb_client.Point("mem").tag("host", "PicoW").field("temperature", data["Temperature"]).field("humidity", data["Humidity"])

    write_api.write(bucket=bucket, org=org, record=dataWrite)

    print("Data written to InfluxDB")


    # Write to log file
    file = open("data.txt", "a")
    file.write(msg.payload.decode())
    ct = datetime.datetime.now()
    file.write(f" {ct.strftime('%Y-%m-%d %H:%M:%S')}")
    file.write("\n")
    file.close()



def main():
    client = connect_mqtt()
    client.subscribe(topic)                     # Subscribe to topic    
    client.on_message = on_message              # Set callback function
    client.loop_forever()


if __name__ == '__main__':
    main()