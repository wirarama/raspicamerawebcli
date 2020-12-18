from picamera import PiCamera,Color
from time import sleep

lokasi = '/var/www/html/img/'
camera = PiCamera()
camera.rotation = 180
camera.resolution = (2592, 1944)
camera.framerate = 15
sleep(2)
camera.capture(lokasi+'max.jpg')

camera.annotate_text = "Mantab Jiwa!!!"
camera.annotate_text_size = 50
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
sleep(2)
camera.capture(lokasi+'text.jpg')

camera.brightness = 70
camera.contrast = 30
sleep(2)
camera.capture(lokasi+'bright.jpg')

camera.image_effect = 'colorswap'
sleep(2)
camera.capture(lokasi+'colorswap.jpg')

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.capture(lokasi+'%s.jpg' % effect)
    sleep(1)
