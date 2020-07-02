#####################################################
# The definedModes python module is the one which
# apply wished modes to images and webcam frames
#####################################################

import cv2

# Specified class to apply defined modes
class definedModesClass:

	# Function to apply the Hue Saturation Lightness (HSV) mode
	@staticmethod
	def hueSaturationLightnessModeFunction(wished_image):

		return cv2.cvtColor(wished_image, cv2.COLOR_BGR2HSV)

	# Function to apply the edge detection mode
	@staticmethod
	def edgeDetectionModeFunction(wished_image):

		return cv2.Canny(wished_image, 100, 300)

	# Function to apply the detailEnhance mode
	@staticmethod
	def detailEnhanceFunction(wished_image):

		return cv2.detailEnhance(wished_image, sigma_s=10, sigma_r=0.15)

	# Function to apply the inverted mode
	@staticmethod
	def invertedModeFunction(wished_image):

		return cv2.bitwise_not(wished_image)

	# Function to apply oil painting Mode
	@staticmethod
	def oilPaintingModeFunction(wished_image):

		return cv2.xphoto.oilPainting(wished_image, 10, 1)

	# Function to apply summer Mode
	@staticmethod
	def summerModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_SUMMER)

	# Function to apply ocean Mode
	@staticmethod
	def oceanModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_OCEAN)

	# Function to apply winter Mode
	@staticmethod
	def winterModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_WINTER)

	# Function to apply bone Mode
	@staticmethod
	def boneModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_BONE)

	# Function to apply cool Mode
	@staticmethod
	def coolModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_COOL)

	# Function to apply rainbow Mode
	@staticmethod
	def rainbowModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_RAINBOW)

	# Function to apply jet Mode
	@staticmethod
	def jetModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_JET)

	# Function to apply hsv Mode
	@staticmethod
	def hsvModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_HSV)

	# Function to apply autumn Mode
	@staticmethod
	def autumnModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_AUTUMN)

	# Function to apply spring Mode
	@staticmethod
	def springModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_SPRING)

	# Function to apply hot Mode
	@staticmethod
	def hotModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_HOT)

	# Function to apply pink Mode
	@staticmethod
	def pinkModeFunction(wished_image):

		return cv2.applyColorMap(wished_image, cv2.COLORMAP_PINK)

	# Function to apply the sketch mode
	@staticmethod
	def sketchModeFunction(wished_image, in_color):

		gray_result, dst_result = cv2.pencilSketch(wished_image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

		if in_color == True:

			return dst_result

		else:

			return gray_result
