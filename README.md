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
  - [ ] Datenbank zum speichern der Messwerte
    - [X] InfluxDB mit Web Interface -> kein weiterer Webserver
      -  User: waldluis
      -  Passwort: 
    - [X] Implementieren
      - Test in dp2.py
      - Schreiben in MQTT Callback
    - [X] Timestamps -> automatisch
  - [X] MQTT Broker Mosquitto zum senden der Messwerte
    - Installiert, autostart
  - [X] Backend zum speichern der Messwerte in der Datenbank und empfangen der Messwerte über MQTT
    - [X] Subscriber wie in Projekt
      - Publisher und Subscriber Beispiel
      - Empfängt Messwerte in JSON Format, Topic: roomMonitor/PicoWDHT22
    - [ ] Beispiele optimieren
  - [X] main.py Autostart
    - rc.local mit 20s delay
    - Delay dass Netzwerk und InfluxDB gestartet sind
  
### Website zum anzeigen der Messwerte

  - [X] Framework informieren
    - InfluxDB Web Interface
    - Eingerichtet
    - Token für Zugriff checken - Token generieren
    - [ ] User nur zum Dashboard anzeigen
    - [X] Dashboard erstellen
  
### Raspberry Pi Pico W

  - [X] Autorun einrichten
    - Alle files mit Thonny Save Copy in Pico
    - Hauptprogramm main.py 
  - [X] MicroPython
    - Einfacher als C++
    - Libraries vorhanden 
  - [X] MicroPython Programm zum auslesen der Messwerte und senden über MQTT
    - [X] MQTT Client zum schicken der Werte
      - Beispiel in mqttPub.py
    - [X] JSON
    - PAHO MQTT Client
    - https://core-electronics.com.au/guides/getting-started-with-mqtt-on-raspberry-pi-pico-w-connect-to-the-internet-of-things/
  - [ ] Sleep Funktion zum Stromsparen mit Timer Interrupt
    - [ ] Timer Interrupt zum messen
    - [ ] Sleep Funktion zum Stromsparen
    - [ ] Sleep und Timer Interrupt kombinieren
    - [ ] Messintervall einstellen (15 Min?)
    - sleep mode mit Real Time Clock
  - [X] DHT22 auslesen
    - [X] 10k Ohm Widerstand benötigt?? -> Nein
    - test/DHT22.py
  
### Hardware besorgen

  - [X] 10k Ohm Widerstand ?? -> Nicht benötigt
  - [ ] 5V Netzteil 

## Notizen
- 
