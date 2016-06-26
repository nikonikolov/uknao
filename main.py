from naoqi import ALProxy
import urllib
from clarifai.client import ClarifaiApi
import time

tts = ALProxy("ALTextToSpeech", "172.20.10.4", 9559)
mem = ALProxy("ALMemory", "172.20.10.4", 9559)

int currVal = 0

while(true):

	 newVal = changemem.getData("LanguageLearner/Index")
	
	if  newVal > currVal :
		currVal = newVal
		doStuff()

	time.sleep(10)
		
		
def  doStuff() :
	# get the image
	tts.say("Getting image")
	myURL = mem.getData("LanguageLearner/ImageURL")
	urllib.urlretrieve(myURL, "C:/Users/Max/Documents/UKNAO/PepperPic.jpg")

	# image processing
	tts.say("Processing image")
	clarifai_api = ClarifaiApi() # assumes environment variables are set.
	result = clarifai_api.tag_images(open('/path/to/local/image.jpeg', 'rb'))
	resultList = result['results'][0]['result']['tag']['classes']

	# Return the result to Pepper
	tts.say("I think this is a " + str(resultsList[0]))
	mem.insertData("LanguageLearner/Object",resultList[0])
