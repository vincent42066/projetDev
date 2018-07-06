from pyb import Pin, Timer


FREQUENCE = 500 # fréquence PWM pour les moteurs
def initMotorA ( f, PWMPin, DirectionPin):
    #generer la PWM sur la pin 11 du shield (PB3)
    p1 = Pin(PWMPin) # initalisation du pin pour contrôler la PWM
    tim1 = Timer(4,freq = f)#initialisation du Timer 4
    ROTATIONA = Pin(DirectionPin, Pin.OUT_PP)

def setPWMA(speed, direction):
    #fonction pour choisir la vitesse et la direction du moteur A
    ch1 = tim1.channel(1, Timer.PWM, pin=p1)# initialisation du canal du timer
    ch1.pulse_width_percent(speed)# Rapport cyclique de la PWM en %
    if (direction == "FOWARD"):
        ROTATIONA.high()# AVANCER
    elif(direction == "BACKWARD"):
        ROTATIONA.low()# RECULER

def initMotorB ( f, PWMPin, DirectionPin):
    #generer la PWM sur la pin 3 du shield (PE5)
    p2 = Pin(PWMPin) # initalisation du pin pour contrôler la PWM
    tim2 = Timer(12,freq = f)#initialisation du Timer 12
    ROTATIONB = Pin(DirectionPin, Pin.OUT_PP)

def setPWMB(speed, direction):
    #fonction pour choisir la vitesse et la direction du moteur B
    ch2 = tim2.channel(2, Timer.PWM, pin=p2)# initialisation du canal du timer
    ch2.pulse_width_percent(speed)# Rapport cyclique de la PWM en %
    if (direction == "FOWARD"):
        ROTATIONB.high()# AVANCER
    elif(direction == "BACKWARD"):
        ROTATIONB.low()# RECULER


initMotorA(FREQUENCE, 'X9', 'X3')
initMotorB(FREQUENCE, 'Y8', 'X4')
#robot turn on himself
setPWMA(50, "FOWARD")
setPWMB(50, "BACKWARD")
