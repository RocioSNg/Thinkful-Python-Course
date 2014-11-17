import authorization
import json
import requests
from urls import *
import argparse
import sys

def make_parser():
	'''Contructs the command line parser'''
	description = "App that interacts with the Twitter API"
	parser = argparse.ArgumentParser(description = description)
  	subparser = parser.add_subparsers(dest="command", help="Available commands")

	#---subparser for the timeline command-------#
	timeline_parser = subparser.add_parser("timeline", help="get the home timeline of the authenticating user")
	
	#---subparser for the get_followers command--#
	get_followers_parser = subparser.add_parser("get_followers", help="Obtain the followers for a specified User")
	get_followers_parser.add_argument("name", help="The Screen name of the Twitter user you want to get followers for")

	#---subparser for the tweet command----------#
	tweet_parser = subparser.add_parser("tweet", help="Update the status (tweet) of the authenticating user")
	tweet_parser.add_argument("text", help="text you would like to include in the status update (tweet).  Limit of 150 words")
	
	return parser
#---Functions that make requests to the Twitter API------#
def timeline():
	'''
	Gets home timeline information for the user, a collection of 
	most recent tweets/retweets by user and users they follow
	No parameters are required
	'''
  	auth = authorization.authorize() 
	response = requests.get(TIMELINE_URL, auth = auth)	# uses OAuth1 instance that is returned to authenticate 
	return json.dumps(response.json(), indent = 4)	# json.dumps formats the output

def get_followers(name):
	'''
	Get folowers of a specified user
	Screen Name needs to be provided
	'''
  	auth = authorization.authorize() 
  	screen_name = {"screen_name" : name }
 	followers_request = requests.get(FOLLOWERS_URL, params = screen_name, auth = auth)
 	return json.dumps(followers_request.json(), indent = 4)

def tweet(text):  
  	'''Updates the status of the user (tweet)'''
	auth = authorization.authorize()	
	status = {"status" : text}
  	post_request = requests.post(POST_REQUEST_URL, params = status, auth = auth)
  	#print json.dumps(post_request.json(), indent = 4)
  	print "You have just sent the following tweet {!r}".format (text)
  
def main():
	'''Main function'''
	auth = authorization.authorize()  # authorizes the application
	print "Authorizing the application"

	#---Create and Use Parsers----#
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])
	arguments = vars(arguments) 	#converts parsed argument into dictionary
	command = arguments.pop("command")

	if command == "timeline":
		print timeline()
	if command == "get_followers":
		followers  = get_followers(**arguments)	#unpacks key value pairs into keyword arguments
  		print followers
		#load = json.loads(followers)
    #print load
  	if command == "tweet":
		tweet(**arguments)

if __name__ == "__main__":
	main()
