from naoqi import ALProxy
import urllib
from clarifai.client import ClarifaiApi
import time

def  doStuff() :
	# get the image
	tts.say("Getting image")
	myURL = mem.getData("LanguageLearner/ImageURL")
	urllib.urlretrieve(myURL, "C:/Users/Max/Documents/My Stuff/UK-NAO-hackathon/PepperPic.jpg")

	# image processing
	tts.say("Processing image")
	clarifai_api = ClarifaiApi() # assumes environment variables are set.
	result = clarifai_api.tag_images(open( "C:/Users/Max/Documents/My Stuff/UK-NAO-hackathon/PepperPic.jpg", 'rb'))
	resultList = result['results'][0]['result']['tag']['classes']

	# Return the result to Pepper
	print str(resultList[0])
	tts.say("I think this is a " + str(resultList[0]))
	mem.insertData("LanguageLearner/Object",resultList[0])


tts = ALProxy("ALTextToSpeech", "172.20.10.4", 9559)
mem = ALProxy("ALMemory", "172.20.10.4", 9559)

currVal = 0

while(True):

	newVal = mem.getData("LanguageLearner/Index")
	
	if  newVal > currVal :
		currVal = newVal
		print currVal
		doStuff()

	time.sleep(10)