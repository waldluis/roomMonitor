import network
import time
import json
from math import sin
from umqtt.simple import MQTTClient
from dht22 import DHT22Sensor

def connectWIFI():
    """
    Connects to a WiFi network using the provided SSID and password.

    Parameters:
    - wifi_ssid (str): The SSID of the WiFi network.
    - wifi_password (str): The password of the WiFi network.

    Returns:
    None
    """
    wifi_ssid = "MartinRouterKing"
    wifi_password = ""

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(wifi_ssid, wifi_password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    print("Connected to WiFi")




# Initialize MQTT Client
broker = "192.168.188.200"
port = 1883
topic = "test"
client_id = "publish123"



def connectMQTT():
    """
    Connects to an MQTT broker and returns the client object.

    Returns:
        client (mqtt_client.Client): MQTT client object.
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


def publish(client):
    """
    Publishes sensor data from DHT22 to the MQTT broker.

    Args:
        client: The MQTT client object.

    Returns:
        None
    """
    sensor = DHT22Sensor()

    while True:
        time.sleep(3)
        sensor.measure()
        msg = json.dumps(sensor.__dht22Data)
        client.publish(topic, msg)

        
        
def run():
    client = MQTTClient(client_id = client_id, server = broker, port = port)
    client.connect()
    while True:
        publish(client)
        
        
if __name__ == '__main__':
    run()


