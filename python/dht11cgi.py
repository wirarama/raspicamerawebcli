#!/usr/bin/python
import sys
import Adafruit_DHT
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\n\n'
print '<h1>Python Script Test</h1>'
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
