#####################################################
# The definedModes python module is the one which
# apply wished modes to images and webcam frames
#####################################################

import cv2

# Function to apply the Hue Saturation Lightness (HSV) mode
def hueSaturationLightnessModeFunction(wished_image):

	return cv2.cvtColor(wished_image, cv2.COLOR_BGR2HSV)

# Function to apply the edge detection mode
def edgeDetectionModeFunction(wished_image):

	return cv2.Canny(wished_image, 100, 300)
