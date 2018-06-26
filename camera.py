import timeit
from picamera import PiCamera
from time import sleep, gmtime

camera = PiCamera()

#camera.start_preview()

timeit.timeit("camera.capture('/home/pi/FacialRecognition/test.jpg')",number=1)

#camera.stop_preview()
