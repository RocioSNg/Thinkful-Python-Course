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

# open cursor
cur = conn.cursor()

#test connection
cur.execute('''select * from breed''')
rows = cur.fetchall()
for row in rows:
	print "   ", row

cur.execute('''select * from species''')
rows = cur.fetchall()
for row in rows:
	print "   ", row

# field names NEED to be changed to reflect SQL file
field_names = ['name', 'age', 'breed', 'species', 'shelter', 'adopted']

#----------opens and parses the CSV file, creating a dictionary of items to be inserted into the database


# open csv file and convert to dictReader object
pet_file = open("pets_to_add.csv")
csv_reader = csv.DictReader(pet_file, delimiter = ',', fieldnames = field_names)

# create list of dictionary items
pets_list = []

for row in csv_reader:
	#print row
	pets_list.append(row)

# change blanks to none
pets_to_add_list = []
for lib in pets_list:
	l = {k:lib[k]  if lib [k] != ""  else None for k in lib}
	pets_to_add_list.append(l)
print pets_to_add_list


# check updates
cur.execute('''select * from pet''')
rows = cur.fetchall()
print rows
#rows = cur.fetchall()
#for row in rows:
#	print row

# Create tuple of all data to be added
pets_to_add =  tuple(pets_to_add_list[1:])	# do not want to include the top row which contain the bad fieldnames
#print pets_to_add

#print pets_to_add[2]
#cur.execute("""INSERT INTO pet(name, age, adopted) VALUES (%(name)s,
 	#%(age)s , %(adopted)s)""", pets_to_add[4])
cur.execute("""INSERT INTO breed(name) VALUES(%(breed)s,
	(SELECT id FROM species WHERE name = %(species)s) )""", pets_to_add[0])



#print pets_to_add[1]


#---------Update tables-------#

# add breed to breed table
#cur.executemany("""INSERT INTO breed(name) VALUES (%(breed)s,
	#(SELECT id FROM species WHERE name = %(species)s) )""", pets_to_add)

# add Pets 
cur.executemany("""INSERT INTO pet(name, age, adopted) VALUES (%(name)s,
	%(age)s , %(adopted)s)""", pets_to_add)


# inserts a new row in the pet table for each dict entry
# missing values as null; normalize for capitalization


# test update

cur.execute('''select * from pet''')
rows2= cur.fetchall()
for row in rows2:
	print row

# Commit changes to the database
conn.commit()
    


