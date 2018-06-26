import subprocess
import numpy as np
from picamera import PiCamera
from time import gmtime, strftime, sleep
from multiprocessing import Pool

default_timestep = 10 # seconds
on = True

# calculate all known faces if not able to archive them

camera = PiCamera()

def captureVideo():
    for np in np.arange(300):
        camera.capture('/home/pi/FacialRecognition/Run/video/frame{}.jpg'.format(str(timestep).zfill(3)))
        sleep(1)

def runFaceRec():
        
    # run face recognition 

    if number_of_friends > 1:
        # say welcome
        name_of_person = 'friend'
        subprocess.call('espeak \"welcome home {}\" 2>/dev/null'.format(name_of_person)        
        # add entry to log
        with open ('access.log','w') as f:
            f.write('{}  |  {}'.format(strftime("%d-%m-%Y %H:%M:%S", gmtime() ), name_of_person))
        # delete stored video
        subprocess.call('rm /home/pi/FacialRecognition/Run/video/*')
        # return to normal scanning
        face_detected = False


    else:
    

while on = True:
    while face_detected = False:
        # slowly capture images
        for n in np.arange(np.floor(600/default_timestep)):            
            camera.capture('/home/pi/FacialRecognition/Run/buffer/image{}.jpg'.format(str(timestep).zfill(2)))
            
            # run face detect script 
            
            sleep(timestep)

              

