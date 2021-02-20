'''
IoT Bootcamp
Trainer: Eng. Meqdad A. Darwish
Phase 2 - Part 3: Working with Sensors and Actuators on Raspberry Pi
Code Sample: Interfacing PIR (Motion Sensor) with Raspberry Pi
'''
from gpiozero import MotionSensor
from time import sleep

pir = MotionSensor(4)  # GPIO4

while True:
    pir.wait_for_motion()
    print('Motion!')
    pir.wait_for_no_motion()
    print('No Motion!')
    # Alternatively, you can use:
    # pir.wait_for_active()
    # pir.wait_for_inactive()
