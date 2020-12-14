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

	# Function to return the current value for voice
	def getVoice(self):

		return self.__engine.getProperty('voice')

	# Function to get all available voices
	def getAllVoices(self):

		voices = self.__engine.getProperty('voices')

		for voice in voices:

			print("Voice: %s" % voice.name)
			print(" - ID: %s" % voice.id)
			print(" - Languages: %s" % voice.languages)
			print(" - Gender: %s" % voice.gender)
			print(" - Age: %s" % voice.age)
			print("\n")

	# Function to set the wished voice identified by its id
	def setVoice(self, voiceId):

		self.__engine.setProperty("voice", voiceId)

	# Function to return the current value of rate
	def getRate(self):

		return self.__engine.getProperty('rate')

	# Function to set a new value for rate
	def setRate(self, rateValue):

		self.__engine.setProperty('rate', rateValue)

	# Function to record a 'wishedText' text inside a 'fileNameWithPath' MP3 file
	def textToSpeechRecorder(wishedText, fileNameWithPath):

		self.__engine.save_to_file(wishedText, fileNameWithPath + '.mp3')
