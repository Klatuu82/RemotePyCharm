import RPi.GPIO as GPIO
import time, datetime

GPIO.setmode(GPIO.BCM)

seg = {'a': 21, 'b': 8, 'c': 11, 'd': 26, 'e': 19, 'f': 20, 'g': 13}
for s in "abcdefg":
    GPIO.setup(seg[s], GPIO.OUT, initial=0)

zif = [16, 12, 7, 6]
for z in zif:
    GPIO.setup(z, GPIO.OUT, initial=1)

zahl = [
    "abcdef",   # 0
    "bc",       # 1
    "abdeg",  # 2
    "abcdg",  # 3
    "bcfg",  # 4
    "acdfg",  # 5
    "acdefg",  # 6
    "abc",  # 7
    "abcdefg",  # 8
    "abcdfg"   #9
]

taster1 = 22
GPIO.setup(taster1, GPIO.IN, GPIO.PUD_DOWN)
taster2 = 27
GPIO.setup(taster2, GPIO.IN, GPIO.PUD_DOWN)

z = [0,0,0,0]

def za():
    for i in range(4):
        for s in "abcdefg":
            GPIO.output(seg[s], 0)
        GPIO.output(zif[i], 0)
        for s in zahl[z[i]]:
            GPIO.output(seg[s], 1)
        time.sleep(0.001)
        GPIO.output(zif[i], 1)


print("Zum Start des Countdowns und zum Neustart Taste 1 drücken")
print("Zum Beenden Taste 2 drücken")

while True:
    timeToXMas = datetime.date(2019, 12, 24) - datetime.date.today()
    daysToXMas = timeToXMas.days
    z[0] = int(daysToXMas / 1000)
    z[1] = int(daysToXMas % 1000 / 100)
    z[2] = int(daysToXMas % 100/ 10)
    z[3] = int(daysToXMas % 10)
    if GPIO.input(taster2) == 1:
        break

    while GPIO.input(taster1)==0 :
        za()
        if GPIO.input(taster2) == 1 :
            break

    while daysToXMas >= 0:
        z[0] = int(daysToXMas / 1000)
        z[1] = int(daysToXMas % 1000 / 100)
        z[2] = int(daysToXMas % 100 / 10)
        z[3] = int(daysToXMas % 10)
        for j in range(100):
            za()
        daysToXMas-=1
        if GPIO.input(taster2) == 1 :
            break

    while GPIO.input(taster1)==0 :
        za()
        if GPIO.input(taster2) == 1 :
            break

GPIO.cleanup()