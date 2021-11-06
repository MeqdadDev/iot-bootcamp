from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.annotate_text = "Added Text"
sleep(5)
camera.capture('text.jpg')
camera.stop_preview()
