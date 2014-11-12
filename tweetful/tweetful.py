import authorization
import json
import requests

from urls import *

def main():
	'''Main function'''
	auth = authorization.authorize()  # authorizes the application
	
  	#---Get Home Timeline information for user---#
  	# Returns a collection of the most recent Tweets and retweets posted by the authenticating user and the users they follow
    
  	response = requests.get(TIMELINE_URL, auth = auth)	# uses OAuth1 instance that is returned to authenticate 
	print json.dumps(response.json(), indent = 4)	# json.dumps formats the output
  
  	#-- Get folowers of a specified user---#
  	#Either a screen_name or a user_id should be provided.
  	screen_name = {"screen_name" : "RocioSNg"}
  	followers_request = requests.get(FOLLOWERS_URL, params = screen_name, auth = auth)
  	print json.dumps(followers_request.json(), indent = 4)
  
  
  
  	#--Post update-----#
    	status = {"status" : "Hello world"}
  	post_request = requests.post(POST_REQUEST_URL, params = status, auth = auth)
    	print json.dumps(post_request.json(), indent = 4)
  
  	#sample post request https://api.twitter.com/1.1/statuses/update.json?status=Maybe%20he%27ll%20finally%20find%20his%20keys.%20%23peterfalk
  
if __name__ == "__main__":
	main()
