import logging
import csv
import argparse
import sys

#------------Set the log output file and the log level---------#
logging.basicConfig(filename="output.log", level=logging.DEBUG)

#-------------Functions----------------------------------------#

def make_parser():
	''' Construct the command line parser'''
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"  # of the program purpose
	parser = argparse.ArgumentParser(description = description)

	subparser = parser.add_subparsers(dest="command", help="Available commands")

	#------Subparser for the put command----------#
	logging.debug("Constructing put subparser")
	put_parser = subparser.add_parser("put", help="Store a snippet")
	put_parser.add_argument("method", help="Add to add a new snippet or Update to update a current snippet")
	put_parser.add_argument("name", help="The name of the snippet")
	put_parser.add_argument("snippet", help="The snippet text")
	put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet file name")	# the nargs='?' allows the argument to be left out and the default value used.

	#------Subparser for the get command----------#
	logging.debug("Constructing get subparser")
	get_parser = subparser.add_parser("get", help="Retrieve snippet text")
	get_parser.add_argument("name", help="the name of the snippet")
	get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The file name containing the snippet")
	
	#------Subparser for the search command--------#
	logging.debug("Constructing the search subparser")
	search_parser = subparser.add_parser("search", help="Searches for snippet containing query string")
	search_parser.add_argument("query", help="the string being looked for")
	search_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The file name being searched")
	return parser

def put(method, name, snippet, filename):	# method either is add or update
	''' Store a snippet with an associated name in the CSV'''
	logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    
	logging.debug("Opening file")
    
	with open(filename, "a") as f:	# 'a' indicates that we want to create a file if it doesn't exist, or append it otherwise
		writer = csv.writer(f)	# writer object will allow for new rows to be added to the CSV file for each created snippet
		#reader = csv.reader(f)
		
		if method in ["add", "Add", "a"]:
			logging.debug("Writing snippet to file")
			writer.writerow([name, snippet])	# adds new rows to the file
			logging.debug("Write successful")
			
		#-----next code block does not work yet------#	
		elif method == "Update":
			logging.debug("Updating snippet in file")
			for row in writer:
				if name == row[0]:
					row[1] = snippet
					logging.debug("Update successful")
		
	return name, snippet #returns a tuple

def get(name, filename):
	'''Retrieves the snippet text associated with the name'''
	logging.info("Retrieving snippet associated with {!r}".format (name))
	logging.debug("Opening File")
	
	
	with open(filename, "r") as r:
		reader = csv.reader(r)
		logging.debug("looking for snippet")
		
		for row in reader:
			if name == row[0]:
				snippet = row[1]
		logging.debug("Snippet Found")
		
	return name, snippet
	#except:
	#	print "snippet not found. Try again"


def search(query, filename):
	'''Finds snippets containing the query string'''
	logging.info("Searching for the snippet containing the string {!r}".format(query))
	logging.debug("Opening File")
	
	results = []  # more than one snippet may satisfy the query
	with open(filename, "r") as r:
		reader = csv.reader(r)
		logging.debug("Searching snippets")
		
		for row in reader:
			if query in row[1]:
				results.append(row[1])
	if len(results) == 0:
		print "The query yielded no results. Try again."
	else: 
		return query, results		
	
def main():
	'''Main function -- runs when command line interface is used'''
	logging.info("Starting Snippets Program")
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])  # passes all the command line arguments except the first which is the name of our program

	# convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")
	if command == "put":
		name, snippet = put(**arguments)   # unpacks key value pairs into keyword arguments
		print "Stored {!r} as {!r}". format(snippet, name)
		
	if command == "get":
		try:
			name, snippet = get(**arguments)
			print "The stored snippet for {!r} is {!r}".format(name, snippet)
		except:
			print "Snippet not Found. Please try again"
			
	if command == "search":
		query, results = search(**arguments)
		if len(results) > 0:
			print "The snippets containing the {!r} string is/are {!r}".format(query, results)

if __name__ == "__main__":
	main()
