# Script to complete psycopg practice assignment

import psycopg2

# Connect to pets database

try:
	conn = psycopg2.connect("dbname = pets", user = "roio", host = "localhost")

except:
	print "I am unable to connect to the database"

# open cursor
cur = conn.cursor()

# test cursor

cur.execute('''select * from breed''')


# open and parse CSV file as dict to be inserted



# inserts a new row in the pet table for each dict entry
# missing values as null; normalize for capitalization

