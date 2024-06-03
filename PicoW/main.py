from dht22 import DHT22Sensor
import time
import json
import machine
from umqtt.simple import MQTTClient
import network



# region Functions

def connectWIFI(wifi_ssid, wifi_password, wlan) -> bool:
    """
    Connects to a WiFi network using the provided SSID and password.

    Args:
        wifi_ssid (str): The SSID of the WiFi network.
        wifi_password (str): The password of the WiFi network.

    Returns:
        None
    """
    counter = 0 
    wlan.active(True)
    wlan.connect(wifi_ssid, wifi_password)
    while wlan.isconnected() == False and counter < 20:
        print('Waiting for connection...')
        time.sleep(1)
        counter += 1
    print("Connected to WiFi")

    if wlan.isconnected():
        return True
    
    return False


def disconnectWIFI(wlan):
    """
    Disconnects from a WiFi network.

    Args:
        wlan (network.WLAN): The WLAN object.

    Returns:
        None
    """
    wlan.disconnect()
    wlan.active(False)
    wlan.deinit()
    print("Disconnected from WiFi")


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
    wlan = network.WLAN(network.STA_IF)
    
    
    # wifi_ssid = "FRITZ!Box 7490_W"
    # wifi_password ="77567930705388833248"

    wifi_ssid = "MartinRouterKing"
    wifi_password = "i_have_a_stream"
    
    connectWIFI(wifi_ssid, wifi_password, wlan)

    broker = "192.168.188.200"
    port = 1883
    client_id = "PicoW_DHT22"
    topic = "roomMonitor/PicoWDHT22"
    client = connectMQTT(broker, port, client_id)

    while True:
        # connect to wifi
        
        sensor.measure()
        
        msg = json.dumps(sensor.getData())
        client.publish(topic, msg)
        
        time.sleep(900)
        
#         if connectWIFI(wifi_ssid, wifi_password, wlan):    
# 
#             # connect to mqtt broker
#             client = connectMQTT(broker, port, client_id)
#             print(client)
#             time.sleep(5)
# 
#             # read sensor data
#             sensor.measure()
# 
#             # publish sensor data
#             msg = json.dumps(sensor.getData())
#             client.publish(topic, msg)
# 
#             # disconnect from mqtt broker
#             client.disconnect()
# 
#             # disconnect from wifi
#             disconnectWIFI(wlan)
# 
#         # sleep for 15 minutes
#         # machine.lightsleep(900_000)
#         time.sleep(60)


if __name__ == "__main__":
    main()
