from dht22 import DHT22Sensor
import time
import json
from umqtt.simple import MQTTClient
import network



# region Functions

def connectWIFI(wifi_ssid, wifi_password):
    """
    Connects to a WiFi network using the provided SSID and password.

    Args:
        wifi_ssid (str): The SSID of the WiFi network.
        wifi_password (str): The password of the WiFi network.

    Returns:
        None
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(wifi_ssid, wifi_password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    print("Connected to WiFi")


def connectMQTT(broker, port, client_id):
    """
    Connects to an MQTT broker.

    Parameters:
    - broker (str): The MQTT broker address.
    - port (int): The port number of the MQTT broker.
    - client_id (str): The client ID for the MQTT connection.

    Returns:
    - client (mqtt_client.Client): The MQTT client object.

    """
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
        
    client = MQTTClient(client_id, broker, port)
    client.on_connect = on_connect
    client.connect()
    return client

# endregion

def main():
    """
    Main function that connects to WiFi, MQTT broker, and publishes sensor data periodically.

    Returns:
        None
    """
    sensor = DHT22Sensor()

    wifi_ssid = "MartinRouterKing"
    wifi_password = "i_have_a_stream"
    connectWIFI(wifi_ssid, wifi_password)

    broker = "192.168.188.200"
    port = 1883
    client_id = "PicoW_DHT22"
    client = connectMQTT(broker, port, client_id)
    topic = "roomMonitor/PicoWDHT22"

    while True:
        sensor.measure()
        msg = json.dumps(sensor.getData())
        client.publish(topic, msg)
        time.sleep(30)


if __name__ == "__main__":
    main()