import urlparse
import requests
from requests_oauthlib import OAuth1   

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *

def get_requests_token():
  '''Get a token allowing us to request user authorization'''
  oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET)  # creates an instance of the OAuth1 class, giving it the client key and secret
  response = requests.post(REQUEST_TOKEN_URL, auth=oauth)  # makes post request passing the oauth object 
  credentials = url.parse_qs(response.content) # response.content is a string that contains request token, this returns a dict with the token and the secret
  
  request_token = credentials.get("oauth_token")[0]  # uses dict.get method to retrience items
  request_secret = credentials.get("oauth_token_secret")[0]
  
  return request_token, request_secret

def authorize():
	'''A complete OAuth authentication flow'''
  	request_token, request_secret = get_request_token()
  	print request_token, request_secret
