#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naoqi import ALProxy
import urllib
from clarifai.client import ClarifaiApi
import time

def  doStuff() :

	# get the image
	tts.say("Downloading image")
	myURL = mem.getData("LanguageLearner/ImageURL")
	urllib.urlretrieve(myURL, "C:/Users/Max/Documents/My Stuff/UK-NAO-hackathon/PepperPic.jpg")

	# image processing
	tts.say("Hmmmm let me see")
	clarifai_api = ClarifaiApi(language="fr") # assumes environment variables are set.
	result = clarifai_api.tag_images(open( "C:/Users/Max/Documents/My Stuff/UK-NAO-hackathon/PepperPic.jpg", 'rb'))
	resultList = result['results'][0]['result']['tag']['classes']
	print resultList

	# Return the result to Pepper
	#print str(resultList[0])
	#tts.say("I think this is a " + str(resultList[0]))
	print "sending word to Pepper:"
	
	try:
		mem.insertData("LanguageLearner/Object",str(resultList[0]))
		print resultList[0]
	except:
		mem.insertData("LanguageLearner/Object",str(resultList[1]))
		print resultList[1]
		


tts = ALProxy("ALTextToSpeech", "172.20.10.4", 9559)
mem = ALProxy("ALMemory", "172.20.10.4", 9559)

mem.insertData("LanguageLearner/Index",0)

currVal = 0

while(True):

	newVal = mem.getData("LanguageLearner/Index")
	
	if  newVal > currVal :
		currVal = newVal
		print  "currVal is "  + str(currVal )+ '\n'
		doStuff()

	time.sleep(5)