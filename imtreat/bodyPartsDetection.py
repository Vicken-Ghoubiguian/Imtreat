##########################################################
# The bodyPartsDetection python module is the one which apply
# wished body parts detection to images and webcam frames
##########################################################

import cv2

# Specified class to apply body parts detections
class bodyPartsDetectionClass:

    # Function to apply face detection
    @staticmethod
    def faceDetectionFunction(wished_image):

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        wished_image_in_gray = cv2.cvtColor(wished_image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(wished_image_in_gray, 1.1, 4)

        for (x, y, w, h) in faces:

            cv2.rectangle(wished_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        return wished_image