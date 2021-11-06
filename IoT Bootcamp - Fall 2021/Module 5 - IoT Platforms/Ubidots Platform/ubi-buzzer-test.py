from gpiozero import Buzzer
from time import sleep
import requests

TOKEN = "BBFF-y1VmdRpiYnFHK4wYJ7SlCvCDW2v4xQ"  # Put your TOKEN here
DEVICE = "buzzer"  # Put your device label here
VARIABLE = "buzzer"  # Put your first variable label here
DELAY = 1
buzzer = Buzzer(17)  # GPIO17


def get_buzzer_status(device, variable):
    try:
        url = f"http://industrial.api.ubidots.com/api/v1.6/devices/{device}/{variable}/"
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        req = requests.get(url=url, headers=headers)
        # print(req)
        # print(req.json()['description'])
        return req.json()['last_value']['value']
    except:
        pass


if __name__ == "__main__":
    while True:
        buzzer_status = get_buzzer_status(DEVICE, VARIABLE)
        print(buzzer_status)
        if buzzer_status == 0:
            buzzer.off()
        elif buzzer_status == 1:
            buzzer.on()
        sleep(DELAY)
