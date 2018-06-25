from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('~/dlib/face_recognition/examples/yuval.jpg')
camera.stop_preview()
