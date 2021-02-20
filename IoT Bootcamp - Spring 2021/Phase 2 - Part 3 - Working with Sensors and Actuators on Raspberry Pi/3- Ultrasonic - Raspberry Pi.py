'''
IoT Bootcamp
Trainer: Eng. Meqdad A. Darwish
Phase 2 - Part 3: Working with Sensors and Actuators on Raspberry Pi
Code Sample: Interfacing Ultrasonic (Distance Sensor) with Raspberry Pi
'''
from gpiozero import DistanceSensor
from time import sleep

ultrasonic = DistanceSensor(echo=17, trigger=4)  # GPIO17 & GPIO4

i = 0

while True:
    print(f"Distance {i} =", format(ultrasonic.distance * 100, '.2f'))
    sleep(1)
    i += 1
