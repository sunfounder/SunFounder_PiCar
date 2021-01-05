import sys
from .import front_wheels
from .import back_wheels
from .SunFounder_PCA9685 import Servo
from .import PCF8591
from .SunFounder_PCA9685 import PCA9685

def servo_install():
    import time
    delay = 1.0/180
    if len(sys.argv) >= 3:
        print("servo-install takes no value")
        usage()
    servoFrontWheel = Servo.Servo(0, bus_number=1)
    servoCamHorizontal = Servo.Servo(1, bus_number=1)
    servoCamVertical = Servo.Servo(2, bus_number=1)
    for i in range(90, -1, -1):
        servoFrontWheel.write(i)
        servoCamHorizontal.write(i)
        servoCamVertical.write(i)
        time.sleep(delay)
    time.sleep(0.1)
    for i in range(0, 181, 1):
        servoFrontWheel.write(i)
        servoCamHorizontal.write(i)
        servoCamVertical.write(i)
        time.sleep(delay)
    time.sleep(0.1)
    for i in range(180, 89, -1):
        servoFrontWheel.write(i)
        servoCamHorizontal.write(i)
        servoCamVertical.write(i)
        time.sleep(delay)
    time.sleep(0.1)
    servoFrontWheel.write(90)
    servoCamHorizontal.write(90)
    servoCamVertical.write(90)
    time.sleep(1)
    print("Servos now are set to 90 degree.")

def main():
    setup()
    if len(sys.argv) >= 2:
        if sys.argv[1] == "servo-install":
            servo_install()
        elif sys.argv[1] == "front-wheel-test":
            if len(sys.argv) >= 3:
                try:
                    chn = int(sys.argv[2])
                except:
                    print("chn must be integer")
                    usage()
                if 0 <= chn <= 15 :
                    front_wheels.test(chn)
                else:
                    print('chn must be in 0~15, not "%s"' % chn)
                    usage()
            front_wheels.test()
        elif sys.argv[1] == "rear-wheel-test":
            back_wheels.test()
        else:
            print('Command error, "%s" is not in list' % sys.argv[1])
            usage()
    else:
        usage()

def usage():
    print("Usage:  picar [Command] [value]")
    print("Commands:")
    print("  servo-install              Set 16 channel servos to 90 degree for installation")
    print("  front-wheel-test [chn]     Test the steering servo connect to chn, chn default 0")
    print("  rear-wheel-test            Test the rear wheel")
    quit()

class ADC(PCF8591.PCF8591):
    pass

def setup():
    pwm=PCA9685.PWM(bus_number=1)
    pwm.setup()
    pwm.frequency = 60
