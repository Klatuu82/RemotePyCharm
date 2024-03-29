import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg={'a':21, 'b':8, 'c':11,'d':26, 'e':19, 'f':20, 'g':13}
for s in "abcdefg":
    GPIO.setup(seg[s], GPIO.OUT, initial=0)

zif=16
GPIO.setup(zif, GPIO.OUT, initial=0)

try:
    while True:
        for s in "cdeg":
            GPIO.output(seg[s], 1)
            time.sleep(0.1)
            GPIO.output(seg[s], 0)

except KeyboardInterrupt:
    GPIO.cleanup()    
