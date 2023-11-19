from machine import Pin
from dht import DHT22


class DHT22Sensor:
    def __init__(self):
        self.__dht22 = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))

        self.__dht22Data = {
            "temperatue": 0.0,
            "humidity": 0.0
        }

    def measure(self):
        self.__dht22.measure()
        self.__dht22Data["temperatue"] = self.__dht22.temperature()
        self.__dht22Data["humidity"] = self.__dht22.humidity()
