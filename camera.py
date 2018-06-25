from picamera import PiCamera
from time import sleep

name = raw_input('Enter name: ')

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/FacialRecognition/face_rec_ex/'+str(name)+'.jpg')
camera.stop_preview()
