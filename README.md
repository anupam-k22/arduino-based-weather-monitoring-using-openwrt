
An embedded systems project that reads live temperature and humidity data
from a DHT11 sensor on an Arduino, and publishes it over MQTT using a
self-hosted broker running on a Raspberry Pi (OpenWRT). 

## Overview
This project demonstrates a small but complete IoT data pipeline:

DHT11 sensor -> Arduino -> USB Serial -> Python bridge -> MQTT publish
                                                              |
                                                              v
                                             Mosquitto broker (Raspberry Pi, OpenWRT)
                                                              |
                                                              v
                                             Subscribers (laptop / phone dashboard app)
