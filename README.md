
An embedded systems project that reads live temperature and humidity data
from a DHT11 sensor on an Arduino, and publishes it over MQTT using a
self-hosted broker running on a Raspberry Pi (OpenWRT). 

## Overview
This project demonstrates a small but complete IoT data pipeline:

DHT11 sensor -> Arduino -> USB Serial -> Python bridge -> MQTT publish -> Mosquitto broker (Raspberry Pi, OpenWRT) -> Subscribers (laptop / phone dashboard app)

Rather than just printing sensor readings to a Serial Monitor, this setup
turns the data into a network-accessible feed that any MQTT client on the
local network can subscribe to in real time.

## Hardware Used


- Arduino Uno 
- DHT11 (temperature/humidity sensor module)
- Raspberry Pi (running OpenWRT)
- Jumper wires
- Ethernet cable

## Software / Tools Used


- Arduino IDE + Adafruit "DHT sensor library"
- Python 3 with pyserial and paho-mqtt
- Mosquitto MQTT broker (installed on the Pi via opkg)
- LuCI web interface and SSH for Pi configuration
- An MQTT client app (IoT MQTT Panel) for phone-based monitoring
                                                              
