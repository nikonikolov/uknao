from naoqi import ALProxy
import urllib
from clarifai.client import ClarifaiApi
import time

def process_to_file(str_data, filename):
	jsonobj = json.loads(str_data)
	utf_list_of_strings = jsonobj['text']
	f = open(filename, 'w')
	for i in utf_list_of_strings:
		f.write(i.encode('utf8'))
	f.close()

def process_to_str(str_data):
	jsonobj = json.loads(str_data)
	utf_list_of_strings = jsonobj['text']
	str_result = ""
	for i in utf_list_of_strings:
		str_result = str_result + i.encode('utf8')
	return str_result

def translate(text, dest_lang, src_lang='en'):
	url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
	values = {	'key' : 'trnsl.1.1.20160625T232425Z.70e416debf73b2a6.1364163d0d7558037cc9fc300df23df12f2ff108',
          		'lang' : src_lang + '-' + dest_lang,
          		'text' : text }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	return response.read()


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

	# Translate result
	unicode_list_of_strings = translate(resultList[0])
	# Return the result to Pepper
	str_result = process_to_str(unicode_list_of_strings)
#	print str(resultList[0])
	tts.say("I think this is a " + str_result)
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