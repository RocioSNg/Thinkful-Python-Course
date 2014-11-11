import urlparse
import requests
from requests_oauthlib import OAuth1   

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *
import json

def get_request_token():
  '''Get a token allowing us to request user authorization'''
  oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET)  # creates an instance of the OAuth1 class, giving it the client key and secret
  response = requests.post(REQUEST_TOKEN_URL, auth=oauth)  # makes post request passing the oauth object 
  credentials = urlparse.parse_qs(response.content) # response.content is a string that contains request token, this returns a dict with the token and the secret
  
  request_token = credentials.get("oauth_token")[0]  # uses dict.get method to retrience items
  request_secret = credentials.get("oauth_token_secret")[0]
  
  return request_token, request_secret

#---- Main Function-----#
def authorize():
	'''A complete OAuth authentication flow'''
	
  	request_token, request_secret = get_request_token()
  	# print request_token, request_secret
 	verifier = get_user_authorization(request_token)
	access_token, access_secret = get_access_token(request_token, request_secret, verifier) # calls our function passing items grabbed

	oauth = OAuth1(CLIENT_KEY, client_secret = CLIENT_SECRET,
			resource_owner_key = access_token,
			resource_owner_secret = access_secret) # new instance which uses our access token and secret for authorization.  Can be used to access APi from elsehwere in our client
	return oauth


def get_user_authorization(request_token):
	'''
	Redirect the user to authorize the client, and then get them to give us
	verification code
	'''
	authorize_url = AUTHORIZE_URL  # not sure why this line is needed yet*****
	authorize_url = authorize_url.format(request_token=request_token) # construct the authorization URL using the request token from twitter
	print "Please go here and authorize:" + authorize_url  # asks the user to visit the authorization URL
	return raw_input("Please input the verifier: ")	# inout the PIN code provided


def get_access_token(request_token, request_secret, verifier):
	'''
	Get a token which will allow us to make requests to the API
	'''
	oauth = OAuth1(CLIENT_KEY,
			client_secret = CLIENT_SECRET,
			resource_owner_key = request_token,
			resource_owner_secret = request_secret,
			verifier = verifier) # new instance Oauth1 which contains client key and secret, AS WELL as our (owner) request token and secret, and verification code from the user
	response = requests.post(ACCESS_TOKEN_URL, auth = oauth) # makes request using th oauth object as authorization credentials
	credentials = urlparse.parse_qs(response.content)
	#--extract the access token and secret--#
	access_token = credentials.get("oauth_token")[0]
	access_secret = credentials.get("oauth_token_secret")[0]
	return access_token, access_secret

#--- get around having to visit the authentification URL every time we use the app

def store_credentials(access_token, access_secret):
	''' Save our access credentials in a json file '''
	with open("access.json", "w") as f:
		json.dump({"access_token": access_token,
				"access_secret": access_secret}, f) # writes a dictionary to the file as JSON

def get_stored_credentials():
	'''Try to retrieve stored access credentials from a json file'''
	with open("access.json", "r") as f:
		credentials = json.load(f)
		return credentials["access_token"], credentials["access_secret"] # reads back from the dictionary
