

from pyb import Pin, Timer

p = Pin('X1') # X1 has TIM2, CH1
tim = Timer(2, freq=1000)
ch = tim.channel(1, Timer.PWM, pin=p)
ch.pulse_width_percent(50)
"""
# Clockwise and counter-clockwise definitions.
# Depending on how you wired your motors, you may need to swap.

ROTATIONA = Pin('X3', Pin.OUT_PP)
ROTATIONA.high()

ROTATIONB = Pin('X4', Pin.OUT_PP)
ROTATIONB.high()

FREQUENCE = 500 # HZ


def initPWM1 ( f):
    #generer la PWM sur la pin 11 du shield (PB3)
    p1 = Pin('X9')
    tim1 = Timer(4,freq = f)

def setPWM1(speed):
    ch1 = tim.channel(1, Timer.PWM, pin=p1)
    ch1.pulse_width_percent(speed)

def initPWM2 ( f):
    #generer la PWM sur la pin 3 du shield (PE5)
    p2 = Pin('Y8')
    tim2 = Timer(12,freq = f)

def setPWM2(speed):
    ch2 = tim.channel(2, Timer.PWM, pin=p2)
    ch2.pulse_width_percent(speed)

initPWM1(FREQUENCE)
initPWM2(FREQUENCE)
setPWM1(50)
setPWM2(50)
