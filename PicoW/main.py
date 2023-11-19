from machine import Pin
from dht import DHT22


class DHT22Sensor:
    """Class representing a DHT22 sensor.

    This class provides methods to measure temperature and humidity using a DHT22 sensor.

    Attributes:
        __dht22: An instance of the DHT22 class.
        __dht22Data: A dictionary to store the measured temperature and humidity.

    """

    def __init__(self):
        self.__dht22 = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))

        self.__dht22Data = {
            "temperature": 0.0,
            "humidity": 0.0
        }

    def measure(self):
        """Measure temperature and humidity.

        This method measures the temperature and humidity using the DHT22 sensor
        and updates the __dht22Data dictionary.

        """
        self.__dht22.measure()
        self.__dht22Data["temperature"] = self.__dht22.temperature()
        self.__dht22Data["humidity"] = self.__dht22.humidity()




def main():
    sensor = DHT22Sensor()
    sensor.measure()
    print(sensor.__dht22Data)

if __name__ == "__main__":
    main()