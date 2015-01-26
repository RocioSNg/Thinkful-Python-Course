# Script to complete psycopg practice assignment

import psycopg2
import csv

# Connect to pets database

try:
	conn = psycopg2.connect("dbname = pets", user = "rocio", host = "localhost")

except:
	print "I am unable to connect to the database"

# open cursor
cur = conn.cursor()

		# test cursor
		# cur.execute('''select * from breed''')


# field names NEED to be changed to reflect SQL file
field_names = ['name', 'age', 'breed_id', 'species_id', 'shelter_id', 'adopted']

#----------opens and parses the CSV file, creating a dictionary of items to be inserted into the database


# open csv file and convert to dictReader object
pet_file = open("pets_to_add.csv")
csv_reader = csv.DictReader(pet_file, delimiter = ',', fieldnames = field_names)

# create list of dictionary items
pets_to_add_list = []

for row in csv_reader:
	#print row
	pets_to_add_list.append(row)

pets_to_add =  tuple(pets_to_add_list[1:])	# do not want to include the top row which contain the bad fieldnames
print pets_to_add

cur.executemany("""INSERT INTO pet(name, age, adopted, breed_id, shelter_id) VALUES (%(name)s,
 	%(age)s , %(adopted)s, %(breed_id)s, %(shelter_id)s""", pets_to_add)


# inserts a new row in the pet table for each dict entry
# missing values as null; normalize for capitalization