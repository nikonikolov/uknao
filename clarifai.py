
from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi() 						# assumes environment variables are set.
result = clarifai_api.tag_images(open('/home/niko/Downloads/image.jpg', 'rb'))

# array of all the recognized objects
objects = result['results'][0]['result']['tag']['classes']

# url example - only publicly accessible urls
#result = clarifai_api.tag_image_urls('http://www.clarifai.com/img/metro-north.jpg')

print objects


