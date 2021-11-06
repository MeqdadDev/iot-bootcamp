'''
IoT Bootcamp
Trainer: Eng. Meqdad A. Darwish
Phase 2 - Part 3: Working with Sensors and Actuators on Raspberry Pi
Code Sample: Interfacing Servo Motor with Raspberry Pi
'''
from gpiozero import Servo
from time import sleep

servo = Servo(4)  # GPIO4

while True:
    servo.mid()
    print("Mid")
    sleep(1)
    servo.max()
    print("Max")
    sleep(1)
    servo.min()
    print("Min")
    sleep(1)
