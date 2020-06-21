################################################
# The vocalAssistant python module defines the
# vocal assistant for the imtreat python package
################################################

import pyttsx3

# Specified class to define the vocal assistance
class vocalAssistantClass:

	# Initialize a vocalAssistantClass instance
	def __init__(self):

		self.__engine = pyttsx3.init()

	# Function to say the text contained in the 'textToSay' variable
	def sayText(self, textToSay):

		self.__engine.say(textToSay)

		self.__engine.runAndWait()

	# Function to return the current value of volume
	def getVolume(self):

		return self.__engine.getProperty('volume')

	# Function to set a new value for volume (value between 0 and 1)
	def setVolume(self, volumeValue):

		if volumeValue >= 0 and volumeValue <= 1.0:

			self.__engine.setProperty('volume', volumeValue)

		else:

			print("Error: invalid value for 'volumeValue'")

	# Function to return the current value of rate
	def getRate(self):

		return self.__engine.getProperty('rate')

	# Function to set a new value for rate
	def setRate(self, rateValue):

		self.__engine.setProperty('rate', rateValue)
