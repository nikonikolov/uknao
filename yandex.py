#import httplib

import urllib
import urllib2
import json
import os
from clarifai.client import ClarifaiApi


def process(str_data, filename):
	jsonobj = json.loads(str_data)
	utf_list_of_strings = jsonobj['text']
	f = open(filename, 'w')
	test_string = ""
	for i in utf_list_of_strings:
		f.write(i.encode('utf8'))
		test_string = test_string + i.encode('utf8')
	f.close()
	print test_string

def translate(text, dest_lang, src_lang='en'):
	url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
	values = {	'key' : 'trnsl.1.1.20160625T232425Z.70e416debf73b2a6.1364163d0d7558037cc9fc300df23df12f2ff108',
          		'lang' : src_lang + '-' + dest_lang,
          		'text' : text }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	return response.read()


def txt_to_speach(filename, lang, outfile):
	cmd = "gtts-cli.py -f " + filename + " -l \'" + lang + "\' " + outfile
	print cmd
	#os.system("gtts-cli.py -f " + filename + " -l \'" + lang + "\' " + outfile)

language = "es"
outfile = "out.txt"
inword = "lady"
filename ="str.txt"

clarifai_api = ClarifaiApi() 						# assumes environment variables are set.
#result = clarifai_api.tag_images(open('/home/niko/Downloads/image.jpg', 'rb'))

# array of all the recognized objects
#objects = result['results'][0]['result']['tag']['classes']
#inword = objects[0]

word = translate(inword, language)
process(word, filename)
txt_to_speach(filename, language, outfile)





"""
conn = httplib.HTTPConnection("www.translate.yandex.net")
conn.request("HEAD","/index.html")
res = conn.getresponse()
print res.status, res.reason
"""

"""
def translate(text, dest_lang, src_lang='en'):
	data = {}
	data['key'] = 'trnsl.1.1.20160625T232425Z.70e416debf73b2a6.1364163d0d7558037cc9fc300df23df12f2ff108'
	data['lang'] = src_lang + '-' + dest_lang
	data['text'] = 'text'
	url_values = urllib.urlencode(data)
	url = 'www.translate.yandex.net/api/v1.5/tr.json/translate'
	full_url = url + '?' + url_values
	data = urllib2.urlopen(full_url)

"""