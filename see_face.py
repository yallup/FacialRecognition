from PIL import Image
import face_recognition

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


def recognise_face_from_locations(image,locations,known_encodings,tolerance):
    for location in locations:
        # Print the location of each face in this image
        # top, right, bottom, left = location
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        encoding = face_recognition.face_encodings(image, location)
        # Loop over each face found in the frame to see if it's someone we know.
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([known_encodings[0]], encoding)
        name = "<Unknown Person>"
        if match[0]:
            name = "Barack Obama"
        print("I see someone named {}!".format(name))


obama_image = face_recognition.load_image_file("face_rec_ex/obama_small.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
known_encodings = [obama_face_encoding]

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("face_rec_ex/two_people.jpg")

did_see, locations = see_face(image)
recognise_face_from_locations(image,locations,known_encodings,0.5)
