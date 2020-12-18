from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
for i in range(5):
    sleep(2)
    camera.capture('/var/www/html/img/image%s.jpg' % i)
