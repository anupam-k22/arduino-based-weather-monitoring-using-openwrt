
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

## How It Works

- Arduino reads temperature and humidity from the DHT11 every 2 seconds
  and prints the values (temp,humidity) over serial monitor.
- A Python script running on a connected computer reads these lines
  over USB serial, parses them, and publishes each value to its own MQTT
  topic via mosquitto_pub.
- The Raspberry Pi, flashed with OpenWRT, runs Mosquitto as a
  local MQTT broker — configured to accept connections from any device
  on the local network.
- Any subscriber on the same network — a command-line client
  (mosquitto_sub) or a phone dashboard app — can view live readings by
  subscribing to these topics:
  sensors/dht11/temperature
  sensors/dht11/humidity
                                                              
