from dht22 import DHT22Sensor

def main():
    sensor = DHT22Sensor()
    sensor.measure()
    print(sensor.__dht22Data)

if __name__ == "__main__":
    main()