import authorization
import json
import requests

from urls import *

def main():
	'''Main function'''
	auth = authorization.authorize()  # authorizes the application
	response = requests.get(TIMELINE_URL, auth = auth)	
	print json.dumps(response.json(), indent = 4)	# json.dumps formats the output

if __name__ == "__main__":
	main()
