#! /usr/bin/python3

# 20180726 - wiki.binefa.cat

# Based on a code from Tony DiCola (AdaFruit)
# License: Public Domain
import time
import Adafruit_ADS1x15
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

p = [0]*4
p[0] = GPIO.PWM(32, 50)  # channel=32 frequency=50Hz
p[1] = GPIO.PWM(33, 50)  # channel=33 frequency=50Hz
p[2] = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p[3] = GPIO.PWM(35, 50)  # channel=35 frequency=50Hz
p[0].start(0)
p[1].start(0)
p[2].start(0)
p[3].start(0)
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
#VPS = 4.096 / 32768.0  #volts per step
VPS = 100.0 / 26600.0 
print('-' * 46)

try:
	values = [0]*4
	while 1:
		for i in range(4):
			values[i] = adc.read_adc(i, gain=GAIN)
			#print('ADC{:01d}: '.format(i)+'HEX 0x{:04x} '.format(values[i])+'DEC {:05d} '.format(values[i])+'reading {:2.3f} %'.format(values[i]*VPS))    
			p[i].ChangeDutyCycle(values[i]*VPS)   
		#print('-' * 46)
		#time.sleep(0.5)
		time.sleep(0.1)

except KeyboardInterrupt:
    pass
p[0].stop()
p[1].stop()
p[2].stop()
p[3].stop()
GPIO.cleanup()
