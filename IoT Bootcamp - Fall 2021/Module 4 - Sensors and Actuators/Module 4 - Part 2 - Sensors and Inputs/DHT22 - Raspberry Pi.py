'''
IoT Bootcamp
Trainer: Eng. Meqdad A. Darwish
Phase 2 - Part 3: Working with Sensors and Actuators on Raspberry Pi
Code Sample: Interfacing DHT22 (Humidity & Temperature Sensor) with Raspberry Pi
'''
from time import sleep
# import Adafruit_DHT # Not supported library (Deprecated)
import adafruit_dht
from board import *

# D4 = GPIO4 / D17 = GPIO17
SENSOR_PIN = D4
dht22 = adafruit_dht.DHT22(SENSOR_PIN, use_pulseio=False)

temperature = dht22.temperature
humidity = dht22.humidity

print(f"Humidity= {humidity:.2f}")
print(f"Temperature= {temperature:.2f}°C")
