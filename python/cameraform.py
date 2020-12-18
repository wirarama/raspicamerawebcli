#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()
from picamera import PiCamera
from time import sleep
alamat = cgi.escape(os.environ["REMOTE_ADDR"])

print 'Content-type: text/html\n\n'
print '<h1>Camera Web Test</h1>'
form = cgi.FieldStorage()
if "jepret" in form:
	camera = PiCamera()
	camera.rotation = 180
	for i in range(int(form["jepret"].value)):
		sleep(2)
		camera.capture('/var/www/html/img/webimage%s.jpg' % i)
	print '<h2>Foto sudah diambil!!!</h2>'
	for i in range(int(form["jepret"].value)):
		print('<h3>Photo ke %s</h3>' % i)
		print('<div><img src="http://%s/img/webimage%s.jpg"></div>' % (alamat,i))
