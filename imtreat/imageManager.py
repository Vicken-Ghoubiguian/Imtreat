import cv2

def openImageFunction(wanted_image, wanted_mode):

	return cv2.imread(wanted_image, wanted_mode)

def displayImageFunction(image_title, wanted_image):

	cv2.imshow(image_title, wanted_image)

def finishItFunction():

	cv2.waitKey(0)

	cv2.destroyAllWindows()
