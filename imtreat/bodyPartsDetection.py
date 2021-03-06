##############################################################
# The bodyPartsDetection python module is the one which apply
# wished body parts detection to images and webcam frames
##############################################################

import cv2

# Specified class to apply body parts detections
class bodyPartsDetectionClass:

    # Function to apply eyes detection
    @staticmethod
    def smileDetectionFunction(wished_image, wished_color = (255, 0, 0)):

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

        wished_image_in_gray = cv2.cvtColor(wished_image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(wished_image_in_gray, 1.1, 4)

        for (fx, fy, fw, fh) in faces:

            roi_gray = wished_image_in_gray[fy:fy + fh, fx:fx + fw]

            roi_color = wished_image[fy:fy + fh, fx:fx + fw]

            smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 4)

            for (sx, sy, sw, sh) in smiles:

                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), wished_color, 2)

        return wished_image

    # Function to apply eyes detection
    @staticmethod
    def eyesDetectionFunction(wished_image, wished_color = (255, 0, 0)):

        eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

        wished_image_in_gray = cv2.cvtColor(wished_image, cv2.COLOR_BGR2GRAY)

        eyes = eyes_cascade.detectMultiScale(wished_image, 1.1, 4)

        for (x,y,w,h) in eyes:

            cv2.rectangle(wished_image, (x ,y),(x+w, y+h), wished_color, 2)

        return wished_image

    # Function to apply face detection
    @staticmethod
    def faceDetectionFunction(wished_image, wished_color = (255, 0, 0)):

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        wished_image_in_gray = cv2.cvtColor(wished_image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(wished_image_in_gray, 1.1, 4)

        for (x, y, w, h) in faces:

            cv2.rectangle(wished_image, (x, y), (x+w, y+h), wished_color, 2)

        return wished_image
