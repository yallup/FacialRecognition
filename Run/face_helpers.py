from PIL import Image
import numpy as np
import face_recognition
from picamera import PiCamera

def take_picam_picture(res):
    camera = PiCamera()
    camera.resolution = (res,res)
    camera.capture(raw_input('Enter name for picture: '))

def see_face(image):
    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as good as CNN.
    # See also: find_faces_in_picture_cnn.py
    locations = face_recognition.face_locations(image)
    if len(locations) != 0:
        did_see = True
    else:
        did_see = False
    return(did_see, locations)

def recognise_face_from_locations(image,locations,known_encodings,toleranceLevel):
    # Print the location of each face in this image
    # top, right, bottom, left = location
    # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    encodings = face_recognition.face_encodings(image, locations)
    print('Encodings '+str(np.shape(encodings[0]))) 
    friends = 0
    names = []
    for encoding in encodings:
        # Loop over each face found in the frame to see if it's someone we know.
        # See if the face is a match for the known face(s)
        for key in known_encodings:
            print(key)
            print(np.shape(known_encodings[key]))
            print(np.shape(encoding))
            match = face_recognition.compare_faces([known_encodings[key]], encoding, tolerance=toleranceLevel)
            if match[0]:
                names.append(key)
                friends += 1
    return friends,names
