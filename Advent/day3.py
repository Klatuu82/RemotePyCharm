import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

rot= 18
gelb = 23
gruen = 24

gpio.setup(rot, gpio.OUT, initial=0)
gpio.setup(gelb, gpio.OUT, initial=0)
gpio.setup(gruen, gpio.OUT, initial=1)

print("Strg+C beendet das Programm")
try:
    while True:
        time.sleep(2)
        gpio.output(gruen, 0)
        gpio.output(gelb, 1)
        time.sleep(0.6)
        gpio.output(gelb, 0)
        gpio.output(rot, 1)
        time.sleep(2)
        gpio.output(gelb, 1)
        time.sleep(0.6)
        gpio.output(rot, 0)
        gpio.output(gelb, 0)
        gpio.output(gruen, 1)

except KeyboardInterrupt:
    gpio.cleanup()
