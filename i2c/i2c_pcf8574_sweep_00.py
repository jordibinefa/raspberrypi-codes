#!/usr/bin/python

import smbus
import time

# i2c address of PCF8574
PCF8574=0x20 # 0x38

# open the bus (0 -- original Pi, 1 -- Rev 2 Pi)
b=smbus.SMBus(1)

byHex=0x00
# make certain the pins are set high so they can be used as inputs
b.write_byte(PCF8574, ~byHex)

byHex=0x01
while 1:
	#pins = b.read_byte(PCF8574)
	#print "%02x" % pins
	b.write_byte(PCF8574, ~byHex)
	print "%02x" % byHex
	byHex = byHex * 2
	time.sleep(0.1)
	if byHex > 0x08:
		byHex=0x01
