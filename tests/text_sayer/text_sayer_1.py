import sys
import imtreat

vocalAssistant = imtreat.vocalAssistant.vocalAssistantClass()

sayText = ""

if len(sys.argv) == 1:

	sayText = "Hello world"

else:

	sayText = sys.argv[1]

vocalAssistant.setVolume(1.0)
vocalAssistant.setRate(50)
vocalAssistant.sayText(sayText)
