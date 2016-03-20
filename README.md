# AD-Converter-for-Openplotter


This script is for controlling more AD converter MCP3008 or MCP3208 with the Raspberry.  
MCP3008 or MCP3208 are AD converters with output SPI interface and 8 analog  10 bits or 12 bits inputs respectively.
The script uses Python SPIDEV library for controlling SPI inteface in Raspberry. The is intended for use with the draft Openplotter, although can be used for other applications with Raspberry
The function Read Chanel (chanel, cs) reads the bits of the MCP3008 0 MCP3208, where -channel- is the input channel (0 to 7) and -cs- is the chip which reads (0 or 1), when two converters are used.
