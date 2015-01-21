# Script to complete psycopg practice assignment

import psycopg2
import csv

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

	#add_pets = csv.reader(open("pets_to_add.csv"))

	#print add_pets[1]


		#pets_to_add_list = ()

		#for row in add_pets:
			#print row
			#inner_dict = dict(zip(fieldnames, values))
			#pets_to_add_list.append(inner_dict)	

	#print pets_to_add_list


pet_file = open("pets_to_add.csv")

field_names = pet_file.readline()
print field_names


#print field_names
csv_reader = csv.DictReader(pet_file, delimiter = ',' )


pets_to_add_list = []

print csv_reader
for row in csv_reader:
	pets_to_add_list.append(row)

pets_to_add =  tuple(pets_to_add_list)



cur.executemany("""INSERT INTO pet(Name, age,
 breed name, species name, shelter name, adopted) VALUES (%s,
 	%s, %s, %s, %s, %s)""", pets_to_add_list)


# inserts a new row in the pet table for each dict entry
# missing values as null; normalize for capitalization