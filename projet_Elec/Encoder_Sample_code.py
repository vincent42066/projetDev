"""
    The sample code for driving one way motor encoder.
    link:
       A pin -- digital 2
       B pin -- digital 4

    See the link for detail:
     http://docs.micropython.org/en/v1.9.3/esp8266/esp8266/tutorial/pins.html
"""

import time
from machine import Pin

encoder0pinA = 0 # A pin -> the interrupt pin
encoder0pinB = 2 # B pin -> the digital pin
encoder0PinALast = None
duration = None
direction = None

def encoderInit():
    direction = True
    pA = Pin(encoder0pinA, Pin.IN)
    pB = Pin(encoder0pinB, Pin.IN)
    p0 = Pin(0, Pin.IN)
    p0.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=wheelSpeed)

def wheelSpeed():
    Lstate = pA.value()
    if((encoder0PinALast == 0) and Lstate== 1):
        val = pB.value()
        if(val == 0 and direction):
            direction = False
        elif(val == 1 and not direction):
            direction = True
    encoder0PinALast = Lstate
    if not direction:
        duration += 1
    else
        duration -= 1

while True:
    print("Pulse: " + duration)
    duration = 0
    time.sleep_ms(100)
