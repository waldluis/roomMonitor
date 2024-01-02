from paho.mqtt import client as mqtt_client
import datetime

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
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
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