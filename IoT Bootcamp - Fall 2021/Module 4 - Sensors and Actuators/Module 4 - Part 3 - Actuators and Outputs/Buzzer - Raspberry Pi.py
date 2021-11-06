'''
IoT Bootcamp
Trainer: Eng. Meqdad A. Darwish
Phase 2 - Part 3: Working with Sensors and Actuators on Raspberry Pi
Code Sample: Interfacing Buzzer with Raspberry Pi
'''
from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)  # GPIO17

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
