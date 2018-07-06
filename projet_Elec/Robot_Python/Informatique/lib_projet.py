
def initMotorA(f, PWMPin, DirectionPin):
    #generer la PWM
    p1 = Pin(PWMPin) #initialisation du Pin
    tim1 = Timer(4,freq = f) #initialisation du timer 4
    ROTATIONA = Pin(DirectionPin, Pin.OUT_PP)

def setPWMA(speed, direction):
    #vitesse et Direction
    ch1 = tim1.channel(1, Timer.PWM, pin=p1) #initialisation du canal du timer
    ch1.pulse_width_percent(speed) #Rapport cyclique de la PWM en %
    if (direction == "FOWARD"):
        ROTATIONA.high() #AVANCER
    elif(direction == "BACKWARD"):
        ROTATIONA.low() #RECULER

#CAPTEUR I2C--------------------------------------------------------------------

import pycom
import time
import machine
from machine import I2C

i2c=I2C(0,I2C.MASTER)
buffer=[2]
phrase=" Lux"

i2c.writeto_mem(0x39,0xA0,bytes([0x03])) #Power On

while True:

    buffer=i2c.readfrom_mem(0x39,0xac,2)
    lux=buffer[0]|buffer[1]<<8
    lux=(40000*lux)/65535
    print (lux," Lux")
    time.sleep(0.25)

    # MOTEUR CC-----------------------------------------------------------------
import machine
from machine import PWM
from machine import Pin

pin23 = Pin('P23', mode=Pin.OUT)
pin22 = Pin('P22', mode=Pin.OUT)
pin21 = Pin('P21', mode=Pin.OUT)
pwm = PWM(0, frequency=500)
pwm.channel(0, pin='P23', duty_cycle=0.5)
pwm.channel(1, pin='P22', duty_cycle=0)

pin21(True)  # sleep mode: high to desactive, down to active

# CAPTEUR I2C + MOTEUR CC-------------------------------------------------------


import pycom
import time
import machine
from machine import I2C
from machine import PWM
from machine import Pin



i2c=I2C(0,I2C.MASTER)
buffer=[2]
phrase=" Lux"

i2c.writeto_mem(0x39,0xA0,bytes([0x03])) #Power On

pin23 = Pin('P23', mode=Pin.OUT)
pin22 = Pin('P22', mode=Pin.OUT)
pin21 = Pin('P21', mode=Pin.OUT)
pwm = PWM(0, frequency=500)


pin21(True)  # sleep mode: high to desactive, down to active


def gauche(event):
        pwm.channel(0, pin='P23', duty_cycle=1)
        pwm.channel(1, pin='P22', duty_cycle=0)

while True:

    buffer=i2c.readfrom_mem(0x39,0xac,2)
    lux=buffer[0]|buffer[1]<<8
    lux=(40000*lux)/65535
    if lux < 1500:
        pwm.channel(0, pin='P23', duty_cycle=0)
        pwm.channel(1, pin='P22', duty_cycle=0)
    else:
        pwm.channel(0, pin='P23', duty_cycle=0)
        pwm.channel(1, pin='P22', duty_cycle=0)

    print (lux," Lux")
    root.bind("<Left>",gauche)
    time.sleep(0.25)

# ROBOT-------------------------------------------------------------------------
# main.py -- put your code here!



import pycom
import time
import machine
from machine import I2C
from machine import PWM
from machine import Pin


pin23 = Pin('P23', mode=Pin.OUT)
pin22 = Pin('P22', mode=Pin.OUT)
pin21 = Pin('P21', mode=Pin.OUT)
pin20 = Pin('P20', mode=Pin.OUT)
pin19 = Pin('P19', mode=Pin.OUT)

pin18 = Pin('P18', mode=Pin.IN)

pwm = PWM(0, frequency=500)

pin21(True)  # sleep mode: high to desactive, down to active


while True:

# 0
# 0.25
# 0.25    reculer
# 0
#
# 0.25
# 0
# 0       avancer
# 0.25
#
# 0
# 0.25
# 0      gauche
# 0.25
#
# 0.25
# 0
# 0.25   droite
# 0


    if pin18() == 1:

        pwm.channel(0, pin='P23', duty_cycle=1)
        pwm.channel(1, pin='P22', duty_cycle=0)
        pwm.channel(2, pin='P20', duty_cycle=0)
        pwm.channel(3, pin='P19', duty_cycle=1)
    else:
        pwm.channel(0, pin='P23', duty_cycle=0)
        pwm.channel(1, pin='P22', duty_cycle=0)
        pwm.channel(2, pin='P20', duty_cycle=0)
        pwm.channel(3, pin='P19', duty_cycle=0)

# PROJET FINAL -----------------------------------------------------------------

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
#?   13
#?   16

    if pin16() == 0:
        if flag ==1:
            droite()
            flag=0

    if pin16() == 1:
        if flag==0:
            recule()
            flag=1

# PROGRAMME 1 CAPTEUR I2C-------------------------------------------------------

import pycom
import time
import machine
from machine import I2C
from machine import PWM
from machine import Pin



i2c=I2C(0,I2C.MASTER)

i2c.writeto_mem(0x39,0xA0,bytes([0x03])) #Power On

pin7 = Pin('P7', mode=Pin.OUT) #moteur A
pin11 = Pin('P11', mode=Pin.OUT) #moteur A
pin5 = Pin('P5', mode=Pin.OUT) #moteur B
pin6 = Pin('P6', mode=Pin.OUT) #moteur B
pwm = PWM(0, frequency=500)


while True:

    buffer=i2c.readfrom_mem(0x39,0xac,2)
    lux=buffer[0]|buffer[1]<<8
    lux=(40000*lux)/65535
    print (lux," Lux")
    if lux < 1500:
        pwm.channel(0, pin='P7', duty_cycle=0)
        pwm.channel(1, pin='P11', duty_cycle=0)
        pwm.channel(2, pin='P5', duty_cycle=0)
        pwm.channel(3, pin='P6', duty_cycle=0)
    else:
        pwm.channel(0, pin='P7', duty_cycle=1)
        pwm.channel(1, pin='P11', duty_cycle=0)
        pwm.channel(2, pin='P5', duty_cycle=1)
        pwm.channel(3, pin='P6', duty_cycle=0)

# PROGRAMME 2 IR----------------------------------------------------------------

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
