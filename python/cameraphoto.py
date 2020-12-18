#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
from picamera import PiCamera
from time import sleep

print 'Content-type: text/html\n\n'
print '<h1>Camera Web Test</h1>'

camera = PiCamera()
camera.rotation = 180
for i in range(5):
	sleep(2)
	camera.capture('/var/www/html/img/webimage%s.jpg' % i)
print '<h2>Foto sudah diambil!!!</h2>'
for i in range(5):
	print('<h3>Photo ke %s</h3>' % i)
	print('<div><img src="http://192.168.1.9/img/webimage%s.jpg"></div>' % i)
