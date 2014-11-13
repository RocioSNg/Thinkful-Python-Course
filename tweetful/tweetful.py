import authorization
import json
import requests
from urls import *

import sys

def make_parser():
	description = "App that interacts with the Twitter API"
	parser = argparse.ArgumentParser(description = description)

	#---subparser for the get_followers command--#
	


#---Functions that make requests to the Twitter API------#
def timeline():
	'''
	Gets home timeline information for the user, a collection of 
	most recent tweets/retweets by user and users they follow
	No parameters are required
	'''
	response = requests.get(TIMELINE_URL, auth = auth)	# uses OAuth1 instance that is returned to authenticate 
	print json.dumps(response.json(), indent = 4)	# json.dumps formats the output

def get_followers(name):
	'''
	Get folowers of a specified user
	Screen Name needs to be provided
	'''
  	auth = authorization.authorize() 
  	screen_name = {"screen_name" : name }
 	followers_request = requests.get(FOLLOWERS_URL, params = screen_name, auth = auth)
 	print json.dumps(followers_request.json(), indent = 4)

def tweet(text):  
  status = {"status" : "Hello world"}
  post_request = requests.post(POST_REQUEST_URL, params = status, auth = auth)
  print json.dumps(post_request.json(), indent = 4)
  
  
def main():
	'''Main function'''
	auth = authorization.authorize()  # authorizes the application
	get_followers("RocioSNg")  	 		  
  	  

if __name__ == "__main__":
	main()
