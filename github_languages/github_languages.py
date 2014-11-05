import sys
import operator
from collections import defaultdict
import requests

from secret import USERNAME, PASSWORD

def get_repositories(user):
	'''Retrieve a list of user's repositories'''
	url = "https://api.github.com/users/{user}/repos".format(user=user)
	response = requests.get(url, auth=(USERNAME, PASSWORD))
	return response.json()

def get_languages_dictionaries(repositories):
  '''
  Return a list of dictionaries containing the languages used in each
  repository
  '''
  language_dictionaries = []
  for repository in repositories:
    url = "https://api.github.co/repos/{owner}/{repo}/languages"
    url = url.format(owner=respository["owner"]["login"],
                     repo=repository["name"])
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    language_dictionaries.append(response.json())
  return language_dictionaries

def main():
	'''Main function'''
	repositories = get_repositories(sys.argv[1])
	language_dictionaries = get_language_dictionaries(respositories)
	print language_dictionaries

if __name__ == "__main__":
	main()

	
