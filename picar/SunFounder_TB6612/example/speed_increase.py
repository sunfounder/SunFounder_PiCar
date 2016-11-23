#!/usr/bin/env python
'''
**********************************************************************
* Filename    : speed_increase.py
* Description : a test script for SunFounder_TB6612 module
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-23    New release
**********************************************************************
'''

import time
from SunFounder_TB6612 import TB6612

def main():
	print "********************************************"
	print "*                                          *"
	print "*           SunFounder TB6612              *"
	print "*                                          *"
	print "*          Connect MA to BCM17             *"
	print "*          Connect MB to BCM18             *"
	print "*         Connect PWMA to BCM27            *"
	print "*         Connect PWMB to BCM12            *"
	print "*                                          *"
	print "********************************************"
	motorA = TB6612.Motor(17, 27)
	motorB = TB6612.Motor(18, 22)
	motorA.set_debug(True)
	motorB.set_debug(True)

	delay = 0.05

	motorA.forward()
	for i in range(0, 101):
		motorA.set_speed(i)
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorA.set_speed(i)
		time.sleep(delay)

	motorA.backward()
	for i in range(0, 101):
		motorA.set_speed(i)
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorA.set_speed(i)
		time.sleep(delay)

	motorB.forward()
	for i in range(0, 101):
		motorB.set_speed(i)
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorB.set_speed(i)
		time.sleep(delay)

	motorB.backward()
	for i in range(0, 101):
		motorB.set_speed(i)
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorB.set_speed(i)
		time.sleep(delay)

def destroy():
	motorA.stop()
	motorB.stop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		destroy()