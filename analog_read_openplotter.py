import spidev
import time
import os
 
# SPI bus
spi = spidev.SpiDev()
# spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
 
def ReadChannel(channel,cs):
  spi.open(0,cs)
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  spi.close()
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
 
# Define sensor channels
pot = 0
 
# Define delay between readings
delay = 2
 
while True:
 
  # Read the light sensor data
  adc = ReadChannel(pot,0)
  adc1 = ReadChannel(1,0)
  adc2 = ReadChannel(2,0)
  adc3 = ReadChannel(3,0)
  adc4 = ReadChannel(4,0)
  adc5 = ReadChannel(5,0)
  adc6 = ReadChannel(6,0)
  adc7 = ReadChannel(7,0)

  bdc = ReadChannel(pot,1)
  bdc1 = ReadChannel(1,1)
  bdc2 = ReadChannel(2,1)
  bdc3 = ReadChannel(3,1)
  bdc4 = ReadChannel(4,1)
  bdc5 = ReadChannel(5,1)
  bdc6 = ReadChannel(6,1)
  bdc7 = ReadChannel(7,1)


  pot_volts = ConvertVolts(adc,2)
  pot_voltsb = ConvertVolts(bdc,2)
 
  # Print out results
  print ("--------------------------------------------")
  print ("Lectura ADC: ", adc, adc1, adc2, adc3, adc4, adc5, adc6, adc7)
  print ("Lectura BDC: ", bdc, bdc1, bdc2, bdc3, bdc4, bdc5, bdc6, bdc7)
  print("Voltaje: {}V".format(pot_volts))
  print("Voltaje: {}V".format(pot_voltsb))

 
  # Wait before repeating loop
  time.sleep(delay)
