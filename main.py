#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naoqi import ALProxy
import urllib
from clarifai.client import ClarifaiApi
import time
import os
import paramiko
from scp import SCPClient

def txt_to_speach_from_file(filename, lang, outfile):
	cmd = "gtts-cli.py -f " + filename + " -l \'" + lang + "\' -o" + outfile
	os.system(cmd)

def txt_to_speach(text, lang, outfile):
	cmd = "gtts-cli.py -t " + text + " -l \'" + lang + "\' -o" + outfile
	os.system(cmd)

"""
def scp(server, port, user, password, filename):
	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, port, user, password)
	# SCPCLient takes a paramiko transport as its only argument
	scp = SCPClient(ssh.get_transport())

	scp.put(filename)
#	scp.get('test2.txt')

	scp.close()


server = "172.20.10.4"
username = "nao"
password = "nao"
port=22
"""


def play_audio(alproxy, text, lang):
	filename = "snd.mp3"	# do remember path!!!
	txt_to_speach(text, lang, filename)
	audio_player = ALProxy("ALAudioPlayer", "172.20.10.4", 9559)
	fileId = audio_player.loadFile("")
	audio_player.play(fileId, _async=True)



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
Status API Training Shop Blog About
