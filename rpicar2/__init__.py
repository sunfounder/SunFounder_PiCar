import sys
import front_wheels
from rpicar2.SunFounder_PCA9685 import Servo

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "servo-install":
            if len(sys.argv) >= 3:
            	print "servo-install takes no value"
                usage()
            Servo.install()
        elif sys.argv[1] == "front-wheel-test":
            if len(sys.argv) >= 3:
                try:
                    chn = int(sys.argv[2])
                except:
            		print "chn must be integer"
                    usage()
                if 0 <= chn <= 15 :
                    front_wheels.test(chn)
                else:
            		print 'chn must be in 0~15, not "%s"' % chn
                    usage()
            front_wheels.test()
        else:
            print 'Command error, "%s" is not in list' % sys.argv[1]
            usage()
    else:
        usage()

def usage():
    print "Usage:  sunfounder-rpicar2 [Command] [value]"
    print "Commands:"
    print "  servo-install              Set 16 channel servos to 90 degree for installation"
    print "  front-wheel-test [chn]     Test the steering servo connect to chn, chn default 0"
    quit()
