import logging
import csv
import argparse
import sys


#------------Set the log output file and the log level---------#

logging.basicConfig(filename="output.log", level=logging.DEBUG)


#-------------Functions----------------------------------------#

def main():
	'''Main function -- runs when command line interface is used'''
	logging.info("Starting Snippets Program")
	parser = make_parser
	arguments = parser.parse_args(sys.argv[1:])  # passes all the command line arguments except the first which is the name of our program


def make_parser():
	''' Construct the command line parser'''
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"  # defines purpose of the program for the user
	parser = argparse.ArgumentParser(description = description)




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

if __name__ == "__main__":
	main()
