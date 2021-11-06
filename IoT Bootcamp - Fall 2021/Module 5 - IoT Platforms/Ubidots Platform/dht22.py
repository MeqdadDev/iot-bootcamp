from time import sleep
# import Adafruit_DHT # Not supported library (Deprecated)
import adafruit_dht
from board import *

def get_temp_and_hum():
    '''This is a function that uses DHT22 sensor,
    It returns two values:
    - float: Temperature
    - float: Humidity
    '''
    SENSOR_PIN = D4
    dht22 = adafruit_dht.DHT22(SENSOR_PIN, use_pulseio=False)
    return dht22.temperature, dht22.humidity