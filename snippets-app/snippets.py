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
	description = "Store and retrieve snippets of text"  # defines purpose of the program for the user
	parser = argparse.ArgumentParser(description = description)
	
	subparser = parser.add_subparsers(dest="commands" help="Available commands")
	
	# Subparser for the put comman
	logging.debug("Constructing put subparser")
	put_parser = subparser.add_parser("put", help="Store a snippet")
	put_parser.add_argument("name", help="The name of the snippet")
	put_parser.add_argument("snippet", help="The snippet text")
	put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")	# the nargs='?' allows the argument to be left out and the default value used.

	return parser

def put(name, snippet, filename):
	""" Store a snippet with an associated name in the CSV
	"""

	logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
	logging.debug("Opening file")
	with open(filename, "a") as f:	# 'a' indicates that we want to creat a file if it doesn't exist, or append it otherwise
		writer = csv.writer(f)	# writer objet will allow for new rows to be added to the CSV file for each created snippet
		logging.debug("Writing snipet to file")
		writer.writerow([name, snippet])	# adds new rows to the file
	logging.debug("Write successful")
	return name, snippet #returns a tuple

def main():
	'''Main function -- runs when command line interface is used'''
	logging.info("Starting Snippets Program")
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])  # passes all the command line arguments except the first which is the name of our program

if __name__ == "__main__":
main()
