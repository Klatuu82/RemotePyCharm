import RPi.GPIO as GPIO
import time, datetime

GPIO.setmode(GPIO.BCM)

seg = {'a':21, 'b':8, 'c':11, 'd':26, 'e':19,
        'f':20, 'g':13}
for s in "abcdefg":
    GPIO.setup(seg[s], GPIO.OUT, initial=1)

zahl = [
        "abcdef", #0
        "bc", #1
        "abdeg", #2
        "abcdg", #3
        "bcfg", #4
        "acdfg", #5
        "acdefg", #6
        "abc", #7
        "abcdefg", #8
        "abcdfg", #9
        ]

taster = 18
GPIO.setup(taster, GPIO.IN, GPIO.PUD_DOWN)

z = [0,0,0,0]


