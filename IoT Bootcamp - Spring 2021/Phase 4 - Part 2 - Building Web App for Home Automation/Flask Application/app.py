'''
IoT Bootcamp
Trainer: Eng. Meqdad A. Darwish
Phase 4 - Part 2: Building Web App for Home Automation
Code Sample: Controlling LED using an HTML page
'''
from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep

app = Flask(__name__)

# Default: GPIO4
led = LED(4)


@app.route('/')
def home():
    led_data = {
        'led_status': 0,
        'pin': 4,
        'action': 'off',
    }

    return render_template('home.html', data=led_data)


@app.route('/<action>')
def action(action):
    led_data = {
        'led_status': 0,
        'pin': 4,
        'action': action,
    }
    if action == 'on':
        led.on()
        print("led_data['pin']", led_data['pin'])
        led_data['led_status'] = 1
    elif action == 'off':
        led.off()
        led_data['led_status'] = 0
    return render_template('home.html', data=led_data)


if __name__ == "__main__":
    app.run(debug=True)
