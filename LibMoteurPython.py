import pyb
import time
# Bit positions in the 74HCT595 shift register output
MOTOR1_A = 2
MOTOR1_B = 3
MOTOR2_A = 1
MOTOR2_B = 4
MOTOR4_A = 0
MOTOR4_B = 6
MOTOR3_A = 5
MOTOR3_B = 7

# Constants that the user passes in to the motor calls
FORWARD = 1
BACKWARD = 2
BRAKE = 3
RELEASE = 4

# Constants that the user passes in to the stepper calls
SINGLE = 1
DOUBLE = 2
INTERLEAVE = 3
MICROSTEP = 4

DC_MOTOR_PWM_RATE = 8000

numOfRegisterPins = 8
registers = [1,1,1,1,1,1,1,1]

def MotorEnable ():
    #setup des entrées/sorties
    clearRegisters() # mettre à O le tableau register
    writeRegisters()# appliquer les changement de register
    MOTORENABLE.low() # Logique inverser je crois
    MOTORLATCH = Pin('X1', Pin.OUT_PP)# Pin 12 sur le shield (RCLK)
    MOTORCLK = Pin('X2', Pin.OUT_PP)# Pin 4 sur le shield (SRCLK)
    MOTORENABLE = Pin('X3', Pin.OUT_PP) # Pin 7 sur le shield
    MOTORDATA = Pin('X4', Pin.OUT_PP)# Pin 8 sur le shield (SER_Pin)

def clearRegisters():
    for i in range(numOfRegisterPins):
        registers[i] = 0

def writeRegisters():
    #Met et affiche les registre sur les sortie du 74HCT595
    #Appeler cette fonction aprés avoir mis les valeurs voulues
    MOTORLATCH.low()
    for i in range(numOfRegisterPins):
        MOTORCLK.low()
        val = registers[i]
        if val == 1:
            MOTORDATA.high()
        elif val == 0:
            MOTORDATA.low()
        else:
            print("Error in variable registers")
        MOTORCLK.high()

def setRegisterPin(index, value):
    registers[index] = value

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


def initPWM3 ( f):
    #generer la PWM sur la pin 6 du shield (PD6)
    p3 = Pin('Y4')
    tim3 = Timer( 4, freq = f)

def setPWM3(speed):
    ch3 = tim.channel(4, Timer.PWM, pin=p3)
    ch3.pulse_width_percent(speed)

def initPWM4 ( f):
    #generer la PWM sur la pin 5 du shield (PE3)
    p4 = Pin('Y6')
    tim4 = Timer( 4, freq = f)

def setPWM4(speed):
    ch4 = tim.channel(3, Timer.PWM, pin=p4)
    ch4.pulse_width_percent(speed)



class DcMotors ():
    def __init__(self, num):
        self.motornum = num
        self.pwmfreq = DC_MOTOR_PWM_RATE
        init()

    def init():
        MotorEnable()
        if self.motornum == 1:
            setRegisterPin(MOTOR1_A, 0)
            setRegisterPin(MOTOR1_B, 0)
            writeRegisters()
            initPWM1(self.pwmfreq)
            a = MOTOR1_A
            b = MOTOR1_B
        elif self.motornum == 2:
            setRegisterPin(MOTOR2_A, 0)
            setRegisterPin(MOTOR2_B, 0)
            writeRegisters()
            initPWM2(self.pwmfreq)
            a = MOTOR2_A
            b = MOTOR2_B
        elif self.motornum == 3:
            setRegisterPin(MOTOR3_A, 0)
            setRegisterPin(MOTOR3_B, 0)
            writeRegisters()
            initPWM3(self.pwmfreq)
            a = MOTOR3_A
            b = MOTOR3_B
        elif self.motornum == 4:
            setRegisterPin(MOTOR4_A, 0)
            setRegisterPin(MOTOR4_B, 0)
            writeRegisters()
            initPWM4(self.pwmfreq)
            a = MOTOR4_A
            b = MOTOR4_B
    def run(cmd):
        if cmd == "FORWARD":
            setRegisterPin(a, 0)
            setRegisterPin(b, 1)
            writeRegisters()
        elif cmd == "BACKWARD":
            setRegisterPin(a, 0)
            setRegisterPin(b, 1)
            writeRegisters()
        elif cmd == "RELEASE":
            setRegisterPin(a, 0)
            setRegisterPin(b, 0)
            writeRegisters()
    def setSpeed(speed):
        if self.motornum == 1:
            setPWM1(speed)
        elif self.motornum == 2:
            setPWM2(speed)
        elif self.motornum == 3:
            setPWM3(speed)
        elif self.motornum == 4:
            setPWM4(speed)
