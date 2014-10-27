#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rocio_000
#
# Created:     17/10/2014
# Copyright:   (c) rocio_000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
sys.path.append("c:Dropbox\\Courses_Seminars\\Thinkful_Python_Course\\Bicycle_OOP")

import bicycle_OOP_classes



#------------------------Universal bike catalog----------------------------------#
bike_catalog = {"Schwinn":[19,100],"Trek":[18,400],"Specialized": [15,900],"Cannondale":[19,200],"Giant":[18,450],"Fuji":[20,50]}  #models with weights and production costs

bike_shop1_inventory = {"Schwinn": 3, "Trek": 1, "Specialized":4, "Cannondale":1, "Giant":2, "Fuji": 1}

bike_shop1 = Bike_Shop("On Two Wheels", bike_shop1_inventory)



bike_shop = bike_shop1
#inventory = Bike_Shop1.bike_inventory(bike_shop1_models)
#for bike in inventory:
 #   print bike.model_name
print bike_shop.bikes
#print bike_prices


print "Welcome to the bicycle shop called: %s" % bike_shop.name

#------Customers-----#
cust1 = Customer("Finn", 200)
cust2 = Customer("Jake", 500)
cust3 = Customer("Marceline", 1000)

customers = [cust1,cust2, cust3]  #List with all the customers

for cust in customers:
    print "The name of the customer is: %s" % cust.name
    afforable_bikes = []
    for bike in bike_shop.bike_prices:
        if bike_shop.bike_prices[bike] <= cust.budget:
            afforable_bikes.append(bike)
    print "The bikes that they can afford are:"
    for bike in afforable_bikes:
        print bike
for model in bike_shop.inventory:
    print "We currently have %s of the %s bike model" % (bike_shop.inventory[model], model)


#for model in bike_shop.inventory:
 #   print "We currently have %s of the %s bike model" % (bike_shop.inventory[model], model)


if __name__ == '__main__':
    main()
