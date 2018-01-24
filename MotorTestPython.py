import LibMoteurPython
import time

moteur = DcMotors(4)

#turn on motor
moteur.setSpeed(200)

moteur.run("RELEASE")

while True:
    print("tick")

    moteur.run("FORWARD")
    for i in range(255):
        moteur.setSpeed(i)
        time.sleep_ms(10)

    for i in range(254,-1,-1):
        moteur.setSpeed(i)
        time.sleep_ms(10)

    print("tock")

    moteur.run("BACKWARD")
    for i in range(255):
        moteur.setSpeed(i)
        time.sleep_ms(10)

    for i in range(254,-1,-1):
        moteur.setSpeed(i)
        time.sleep_ms(10)

    print("tech")
    moteur.run("RELEASE");
    time.sleep_ms(1000)
