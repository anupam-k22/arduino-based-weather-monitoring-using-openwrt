import serial
import paho.mqtt.client as mqtt

SERIAL_PORT = "COM3"      # check Arduino IDE's Tools > Port, for the exact name
BAUD_RATE = 9600
MQTT_BROKER = "192.168.1.81"   # your Pi's current IP 
MQTT_PORT = 1883
TOPIC_TEMP = "sensors/dht11/temperature"
TOPIC_HUMIDITY = "sensors/dht11/humidity"

def main():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    print(f"Reading {SERIAL_PORT}, publishing to {MQTT_BROKER}...")

    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if "," in line:
                temp_str, humidity_str = line.split(",")
                try:
                    temp = float(temp_str)
                    humidity = float(humidity_str)
                    client.publish(TOPIC_TEMP, temp)
                    client.publish(TOPIC_HUMIDITY, humidity)
                    print(f"Temp: {temp}C  Humidity: {humidity}%")
                except ValueError:
                    pass  # skip malformed lines
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        ser.close()
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
