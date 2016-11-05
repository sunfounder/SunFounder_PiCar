import sys
import front_wheels
from SunFounder.PCA9685 import Servo

def main():
    """Entry point for the application script"""
    print("Call your main application code here")
    if lenth(sys.argv) > 2:
    	if sys.argv[1] == "servo-install":
    		if lenth(sys.argv) > 3:
    			usage()
			Servo.install()
    	elif sys.argv[1] == "front-wheel-test":
    		if lenth(sys.argv) > 3:
    			try:
    				chn = int(sys.argv[2])
    			except:
    				usage()
    			if 0 < chn < 16 :
    				front_wheels.test(chn)
    			else:
    				usage()
    		front_wheels.test()
    	else:
    		usage()
    else:
    	usage()

def usage():
	print "Usage:  sunfounder-rpicar2 [Command] [value]"
	print "Commands:"
	print "    servo-install                Set 16 channel servos to 90 degree for installation"
	print "    front-wheel-test [chn]       Test the front wheel steering servo connect to chn, chn default 0"
	quit()
