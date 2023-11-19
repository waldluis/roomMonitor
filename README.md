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
  - 
### Raspberry Pi 4

  - [X] Virtual Environment einrichten
  - [ ] Datenbank SQLite3 zum speichern der Messwerte
    - [ ] Informieren
    - [ ] Implementieren
    - [ ] Bilal Projekt
    - [ ] Timestamps
  - [X] MQTT Broker Mosquitto zum senden der Messwerte
    - Installiert, autostart
  - [ ] Backend zum speichern der Messwerte in der Datenbank und empfangen der Messwerte über MQTT
    - [ ] Client wie in Projekt
      - Publisher und Subscriber Beispiel
    - [ ] Beispiele optimieren
  
### Website zum anzeigen der Messwerte

  - [ ] Framework informieren
  - [ ] Website erstellen 
  
### Raspberry Pi Pico W

  - [X] Autorun einrichten
    - Alle files mit Thonny Save Copy in Pico
    - Hauptprogramm main.py 
  - [X] MicroPython
    - Einfacher als C++
    - Libraries vorhanden 
  - [ ] MicroPython Programm zum auslesen der Messwerte und senden über MQTT
    - [ ] MQTT Client zum schicken der Werte
      - Beispiel in mqttPub.py
    - [ ] JSON oder nur String
    - PAHO MQTT Client
  - [ ] Sleep Funktion zum Stromsparen mit Timer Interrupt
    - [ ] Timer Interrupt zum messen
    - [ ] Sleep Funktion zum Stromsparen
    - [ ] Sleep und Timer Interrupt kombinieren
    - sleep mode mit Real Time Clock
  - [X] DHT22 auslesen
    - [X] 10k Ohm Widerstand benötigt?? -> Nein
    - test/DHT22.py
  
### Hardware besorgen

  - [X] 10k Ohm Widerstand ?? -> Nicht benötigt
  - [ ] 5V Netzteil 

## Notizen
- 