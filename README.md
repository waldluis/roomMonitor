# roomMonitor

## Hardware
- Raspberry Pi 4
- Raspberry Pi Pico W
- DHT22 Temperatur- und Luftfeuchtigkeitssensor
- 10k Ohm Widerstand ??
- Breadboard
- 5V Netzteil
  
## Software

### Raspberry Pi 4
- Datenbank SQLite3 zum speichern der Messwerte
- MQTT Broker Mosquitto zum senden der Messwerte
- Backend zum speichern der Messwerte in der Datenbank und empfangen der Messwerte über MQTT
- Webserver zum anzeigen der Messwerte

### Raspberry Pi Pico W
- C++ Programm zum auslesen der Messwerte und senden über MQTT
- Sleep Funktion zum Stromsparen mit Timer Interrupt
- MQTT Client zum senden der Messwerte

## Hardware Setup


## TODOs
- [X] GIT einrichten
  - roomMonitor
  - [X] gitignore
- [ ] Raspberry Pi 4
  - [ ] Virtual Environment einrichten
  - [ ] Datenbank SQLite3 zum speichern der Messwerte
    - [ ] Informieren
    - [ ] Implementieren
    - [ ] Bilal Projekt
    - [ ] Timestamps
  - [ ] MQTT Broker Mosquitto zum senden der Messwerte
    - [ ] Bilal Projekt 
  - [ ] Backend zum speichern der Messwerte in der Datenbank und empfangen der Messwerte über MQTT
    - [ ] Client wie in Projekt
- [ ] Website zum anzeigen der Messwerte
  - [ ] Framework informieren
  - [ ] Website erstellen 
- [ ] Raspberry Pi Pico W
  - [ ] C++ Programm zum auslesen der Messwerte und senden über MQTT
    - [ ] MQTT Client zum schicken der Werte
    - [ ] JSON oder nur String
    - PAHO MQTT Client
  - [ ] Sleep Funktion zum Stromsparen mit Timer Interrupt
    - [ ] Timer Interrupt zum messen
    - [ ] Sleep Funktion zum Stromsparen
    - [ ] Sleep und Timer Interrupt kombinieren
    - sleep mode mit Real Time Clock
    - https://www.heise.de/blog/Sleepy-Pico-ein-Raspberry-Pi-Pico-geht-mit-C-C-schlafen-6046517.html
  - [ ] DHT22 auslesen
    - [X] 10k Ohm Widerstand benötigt?? -> Nein
    - https://github.com/eleanor-em/pico-dht22/blob/main/src/dht22-pico.h
- [ ] Hardware besorgen
  - [X] 10k Ohm Widerstand ?? -> Nicht benötigt
  - [ ] 5V Netzteil 

## Notizen
- 