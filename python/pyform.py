#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\n\n'
print '<h1>Python Form Test</h1>'
form = cgi.FieldStorage()
if "test" not in form:
	print("<h3>Form kosong!</h3>")
else:
	print("<h3>Test: %s </h3>" % form["test"].value)
