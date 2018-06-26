from PIL import Image
import face_recognition
from cv2 import VideoCapture
from picamera import PiCamera

def take_webcam_picture():
    camera = VideoCapture(0)
    retval,image = camera.read()
    del camera
    return image

def take_picam_picture(res):
    camera = PiCamera()
    camera.resolution = (res,res)
    camera.capture(raw_input('Enter name for picture: '))

def see_face(image):

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as good as CNN.
    # See also: find_faces_in_picture_cnn.py
    locations = face_recognition.face_locations(image)
    if locations[0] != 0:
        did_see = True
    else:
        did_see = False
    return(did_see, locations)


def recognise_face_from_locations(image,locations,known_encodings,toleranceLevel):
    # Print the location of each face in this image
    # top, right, bottom, left = location
    # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    encodings = face_recognition.face_encodings(image, locations)
    friends = 0
    names = np.empty(len(known_encodings))
    for encoding in encodings:
    # Loop over each face found in the frame to see if it's someone we know.
    # See if the face is a match for the known face(s)
    for key in known_encodings:
    match = face_recognition.compare_faces([known_encodings[key]], encoding, tolerance=toleranceLevel)
    if match[0]:
        friends += 1
	    names.append(key)
    return friends,names
