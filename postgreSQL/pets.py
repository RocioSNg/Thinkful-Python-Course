# Script to complete psycopg practice assignment

import psycopg2
import csv

# Connect to pets database
con = None

try:
	conn = psycopg2.connect("dbname = pets", user = "rocio", host = "localhost")
	# open curo
	cur = conn.cursor()
	cur.execute('SELECT version()')          
	ver = cur.fetchone()
	print ver    
except:
	print "I am unable to connect to the database"


#test connection
cur.execute('''select * from breed''')
rows = cur.fetchall()
for row in rows:
	print "   ", row

# field names changed for easier updating
field_names = ['name', 'age', 'breed', 'species', 'shelter', 'adopted']

#----------opens and parses the CSV file, creating a dictionary of items to be inserted into the database


# open csv file and convert to dictReader object
pets_list = []
with open("pets_to_add.csv") as pet_file:
#csv_reader = csv.DictReader(pet_file, delimiter = ',')
	reader = csv.DictReader(pet_file, delimiter = ',', fieldnames = field_names)
	next(reader)	# skip header row
	for row in reader:  # each row is a dictionary
		# row = row.strip()
		pets_list.append(row)

#csv_reader = (dict((k, v.strip()) for k, v in row.items() if v) for row in reader)

# create list of dictionary items

print pets_list

# Format the values in each dictionary to match SQL  file specififications
pets_to_add_list = []
for lib in pets_list:
	strip = {k: lib[k].strip() for k in lib}  # get rid of leading spaces
	capt = {k:strip[k].title()  if k != "shelter" else strip[k] for k in strip}  # normalize capitilization
	l = {k:capt[k]  if capt[k] != ""  else None for k in capt}
	pets_to_add_list.append(l)
print pets_to_add_list


# Create tuple of all data to be added
pets_to_add =  tuple(pets_to_add_list[0:])	
#print pets_to_add


#---------Update tables-------#

# tests for single entries
#print pets_to_add[2]
cur.executemany("""INSERT INTO pet(name, age, adopted, breed_id) VALUES (%(name)s,
	%(age)s , %(adopted)s, (SELECT breed.id from breed, 
		species WHERE breed.name = %(breed)s AND species.name = %(species)s AND breed.species_id = species.id  ))""", pets_to_add)

# check updates
cur.execute('''select * from pet''')
rows = cur.fetchall()
for row in rows:
	print "   ", row

#cur.execute("""INSERT INTO pet(name, age, adopted) VALUES (%(name)s,
 	#%(age)s , %(adopted)s)""", pets_to_add[4])
#cur.execute("""INSERT INTO breed(name, species_id) VALUES(%(breed)s,
#	(SELECT id FROM species WHERE name = %(species)s) )""", pets_to_add[0])

# add Pets to pet table.  Get breed ids from breed table
#cur.executemany("""INSERT INTO pet(name, age, adopted, breed_id) VALUES (%(name)s,
#	%(age)s , %(adopted)s, (SELECT id from breed WHERE name = %(breed)s ))""", pets_to_add)

# check updates
cur.execute('''select * from pet''')
rows = cur.fetchall()
for row in rows:
	print "   ", row

# add breed to breed table.  Get species id from species table
cur.executemany("""INSERT INTO breed(name, species_id) VALUES (%(breed)s,
	(SELECT id FROM species WHERE name = %(species)s) )""", pets_to_add)


# add shelters
cur.executemany("""INSERT INTO shelter(name) VALUES (%(shelter)s)""", pets_to_add)



# add Pets to pet table.  Get breed ids from breed table
cur.executemany("""INSERT INTO pet(name, age, adopted, breed_id) VALUES (%(name)s,
	%(age)s , %(adopted)s, (SELECT id from breed WHERE name = %(breed)s ))""", pets_to_add)

# check updates
cur.execute('''select * from pet''')
rows = cur.fetchall()
for row in rows:
	print "   ", row


# Commit changes to the database
conn.commit()
    


