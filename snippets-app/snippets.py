import logging
import csv

# Set the log output file and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


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
