import RPi.GPIO as gpio
import time

def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(4, gpio.OUT)
    gpio.setup(18, gpio.IN)

    gpio.output(18, False)
    while gpio.input(18) == 0:
            nosig = time.time()
    
    while GPIO.input(4) == 1:
        sig  = time.time()

    tl = sig  - nosig
        
    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print ('improper measurement choice of measurement: in or cm')
        distance = None

    gpio.cleanup()
    return distance
    
print (distance, 'cm')

