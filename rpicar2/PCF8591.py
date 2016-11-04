#!/usr/bin/env python
'''
**********************************************************************
* Filename    : PCF8591
* Description : A module to read the analog value with ADC PCF8591
* Author      : Dream
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-09-19    New release
**********************************************************************
'''
import smbus
import time

bus = smbus.SMBus(1)

class PCF8591(object):
	""" Light_Follow Module class """
	def __init__(self, addr=0x48):
		super(PCF8591, self).__init__()
		self.address = addr

	def read(self, chn): #channel
		if chn == 0:
			bus.write_byte(self.address,0x43)
		if chn == 1:
			bus.write_byte(self.address,0x42)
		if chn == 2:
			bus.write_byte(self.address,0x41)
		if chn == 3:
			bus.write_byte(self.address,0x40)
		bus.read_byte(self.address) # dummy read to start conversion
		return bus.read_byte(self.address)

def test():
	ADC = PCF8591(0x48)
	while True:
		A0 = ADC.read(0)
		A1 = ADC.read(1)
		A2 = ADC.read(2)

		print "A0 = %d  A1 = %d  A2 = %d"%(A0,A1,A2)
		time.sleep(0.5)

def destroy():
	pass

if __name__ == '__main__':
	try:
		test()
	except KeyboardInterrupt:
		destroy()