######################################################
# The generalSettings python module returns all
# general settings about python imtreat package
######################################################

import cv2

# Function to open a title-specified image with a specified mode
def openImageFunction(wanted_image, wanted_mode):

	return cv2.imread(wanted_image, wanted_mode)

# Function to display an image in a title-specified window
def displayImageFunction(image_title, wanted_image):

	cv2.imshow(image_title, wanted_image)

# Function to finish loop process
def finishItFunction():

	cv2.waitKey(0)

	cv2.destroyAllWindows()

# Function to save image at a specific path, with a specific title and to a specific format
def saveImageFunction(image_path, image_title, image_format, wished_image):

	cv2.imwrite(image_path + image_title + image_format, wished_image)
