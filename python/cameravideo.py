from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.start_recording('/var/www/html/img/video.h264')
sleep(5)
camera.stop_recording()
