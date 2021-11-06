'''
IoT Bootcamp
Trainer: Eng. Meqdad A. Darwish
Phase 2 - Part 3: Working with Sensors and Actuators on Raspberry Pi
Code Sample: Interfacing LED with Raspberry Pi
'''
from gpiozero import LED
from time import sleep

led = LED(27)  # GPIO27

# LED Blinking
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    # Or you can use blink()
    # led.blink()
