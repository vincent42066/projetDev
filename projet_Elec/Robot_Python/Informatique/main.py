import pycom
import time
import machine
from machine import I2C
from machine import PWM
from machine import Pin

def gauche():
    pwm.channel(0, pin='P7', duty_cycle=0)
    pwm.channel(1, pin='P11', duty_cycle=1)
    pwm.channel(2, pin='P5', duty_cycle=1)
    pwm.channel(3, pin='P6', duty_cycle=0)

def droite():
    pwm.channel(0, pin='P7', duty_cycle=1)
    pwm.channel(1, pin='P11', duty_cycle=0)
    pwm.channel(2, pin='P5', duty_cycle=0)
    pwm.channel(3, pin='P6', duty_cycle=1)

def avance():
    pwm.channel(0, pin='P7', duty_cycle=1)
    pwm.channel(1, pin='P11', duty_cycle=0)
    pwm.channel(2, pin='P5', duty_cycle=1)
    pwm.channel(3, pin='P6', duty_cycle=0)

def recule():
    pwm.channel(0, pin='P7', duty_cycle=0)
    pwm.channel(1, pin='P11', duty_cycle=1)
    pwm.channel(2, pin='P5', duty_cycle=0)
    pwm.channel(3, pin='P6', duty_cycle=1)

def stop ():
    pwm.channel(0, pin='P7', duty_cycle=0)
    pwm.channel(1, pin='P11', duty_cycle=0)
    pwm.channel(2, pin='P5', duty_cycle=0)
    pwm.channel(3, pin='P6', duty_cycle=0)


# 192.168.4.1

pin7 = Pin('P7', mode=Pin.OUT) #moteur A
pin11 = Pin('P11', mode=Pin.OUT) #moteur A
pin5 = Pin('P5', mode=Pin.OUT) #moteur B
pin6 = Pin('P6', mode=Pin.OUT) #moteur B

pin16 = Pin('P16', mode=Pin.IN, pull=Pin.PULL_UP) #capteur
pin15 = Pin('P15', mode=Pin.IN, pull=Pin.PULL_UP) #capteur
pin14 = Pin('P14', mode=Pin.IN, pull=Pin.PULL_UP) #capteur
pin13 = Pin('P13', mode=Pin.IN, pull=Pin.PULL_UP) #capteur

pwm = PWM(0, frequency=500)
flag=1
# pin21(True)   sleep mode: high to desactive, down to active

while True:

# capteur ir
#14   15
#16   13

    while pin14() == 0 and pin15() == 0:
        droite()
    while pin13() == 0 and pin16() == 0:
        gauche()
    stop()
