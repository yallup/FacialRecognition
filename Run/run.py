import os
import face_recognition
import glob
import numpy as np
from picamera import PiCamera
from time import gmtime, strftime, sleep
from multiprocessing import Pool
from face_helpers import see_face, recognise_face_from_locations

default_timestep = 10 # seconds
on = True

# calculate all known faces if not able to archive them
trusted_faces = {}
friend_list = [x.split('/')[-1] for x in glob.glob('../FaceDict/*')]

for friend in friend_list:
    filename = glob.glob('../FaceDict/{}/*'.format(friend))[0]
    image = face_recognition.load_image_file(filename)
    trusted_faces[friend]  = face_recognition.face_encodings(image)[0]


camera = PiCamera()

def captureVideo():
    for np in np.arange(300):
        camera.capture('/home/pi/FacialRecognition/Run/video/frame{}.jpg'.format(str(timestep).zfill(3)))
        sleep(1)

def runFaceRec(current_image, loc, trusted_faces):
    print('HomeID  |  Starting facial recognition')
    # run face recognition 
    number_of_friends, friend_names  = recognise_face_from_locations(current_image, loc, trusted_faces, 0.55)
    
    if number_of_friends >= 1:
        # say welcome
        if number_of_friends == 1:  
            print('HomeID  |  1 Friend')
            os.system('espeak \"welcome home {}\" 2>/dev/null'.format(friend_names[0]))
        else:
            print('HomeID  |  More than one friend')
            s = ' , '.join([n for n in friend_names[:-1]])+' and '+friend_names[-1]
            os.system('espeak \"welcome home {}\" 2>/dev/null'.format(s) )

        
        # add entry to log
        with open ('access.log','w') as f:
            f.write('{}  |  {}'.format(strftime("%d-%m-%Y %H:%M:%S", gmtime() ), friend_names))
        # delete stored video
        # os.system('rm /home/pi/FacialRecognition/Run/video/*')
        # return to normal scanning
        face_trusted = True

    else:
        print('HomeID  |  intruder detected')
        os.system('espeak \"INTRUDER ALERT\" 2>/dev/null')        
    
        face_trusted = False

    face_detected = False
    return face_trusted, face_detected

face_detected = False
while on == True:
    print('HomeID Loaded...')
    while face_detected == False:
        # slowly capture images
        for n in np.arange(np.floor(600/default_timestep)):            
            fname = '/home/pi/FacialRecognition/Run/buffer/image{}.jpg'.format(str(int(n)))
            camera.capture(fname)
            current_image = face_recognition.load_image_file(fname)
            face_detected, loc = see_face(current_image) 
            print(face_detected)
            if face_detected: break
            
    print('Face found')

    p = Pool(processes=2)          

    #vid = p.apply_async(captureVideo)
    rec = p.apply_async(runFaceRec,args=(current_image,loc,trusted_faces)) 
    face_trusted, face_detected = rec.get()
    
    #os.system('ffmpeg -r 1 -i video/frame%01d.jpg -vcodec mpeg4 -y intruder.mp4')

    if face_trusted == False: 
        # os.system('fbi -a '+ fname)
