from PIL import Image
import face_recognition

def see_face(image_name):
  # Load the jpg file into a numpy array
  image = face_recognition.load_image_file(image_name)

  # Find all the faces in the image using the default HOG-based model.
  # This method is fairly accurate, but not as good as CNN.
  # See also: find_faces_in_picture_cnn.py
  face_locations = face_recognition.face_locations(image)
  if face_locations[0] != 0:
    did_see = True
  else:
    did_see = False

  return(did_see, face_locations)
