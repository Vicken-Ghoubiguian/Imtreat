######################################################
# The generalSettings python module returns all
# general settings about python imtreat package
######################################################

import cv2
import numpy
import pyttsx3

# Specified class to consult settings
class generalSettingsClass:

	# Function to check OpenCV current version used by package
	@staticmethod
	def cv2Version():

		return cv2.__version__

	# Function to check NumPy current version used by package
	@staticmethod
	def numpyVersion():

		return numpy.__version__
