#-------------------------------------------------------------------------------
# Name:        Bicycle Industry Classes
# Purpose:  Define classes for Bicycle Industry Modelling Project
#
# Author:      Rocio Ng
# Created:     16/10/2014
#-------------------------------------------------------------------------------

import random

class Bicycle(object):
    def __init__(self, model_name, weight, production_cost, wheel_type, frame_type):
        self.model_name = model_name
        self.weight = weight  # in pounds
        self.production_cost = production_cost

class Wheel(object):
    def __init__(self, model_name, weight, production_cost):
        self.model_name = model_name
        self.weight = weight # in pounds
        self.production_cost = production_cost

class Frame(object):
    def __init__(self, metal_type, weight, production_cost):
        self.metal_type = metal_type
        self.weight = weight
        self.production_cost = production_cost


class Bike_Shop(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory    # dictionary of models of bikes and their inventory numbers
        self.bikes = self.bike_list(inventory)
        self.bike_prices = self.bike_sell_price(self.bikes)

    def bike_list(self,inventory):
        bikes = []
        for key in inventory:
            #item = "Schwinn"
            bike = Bicycle(key, bike_catalog[key][0],bike_catalog[key][1])  # grabs the info from the bike catalog to make instances of each bike
            bikes.append(bike)   # adds each bike to the inventory
        return bikes
        #return inventory ## not necessary
        #self.bike_list = bike_list

    def bike_sell_price(self, bike_list):
        '''determines selling price for each bike
        which is 20% higher than production costs'''
        bike_store_prices= {}
        for item in bike_list:
            bike_store_prices[item.model_name] = item.production_cost + (item.production_cost*.2)
        return bike_store_prices
        #self.bike_prices = bike_store_prices

class Customer(object):
    can_buy_bike = True
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget


#------------------------Universal bike catalog----------------------------------#
bike_catalog = {"Schwinn":[19,100],"Trek":[18,400],"Specialized": [15,900],"Cannondale":[19,200],"Giant":[18,450],"Fuji":[20,50]}  #models with weights and production costs

bike_shop1_inventory = {"Schwinn": 2, "Trek": 1, "Specialized":4, "Cannondale":1, "Giant":1, "Fuji": 2}

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


customer_bikes = {}  # to a dictionary of of customers and the bikes that they can afford
profit = 0

for cust in customers:
    print "The name of the customer is: %s" % cust.name
    affordable_bikes = []
    for bike in bike_shop.bike_prices:
        if bike_shop.bike_prices[bike] <= cust.budget:
            affordable_bikes.append(bike)
    customer_bikes[cust.name] = affordable_bikes
    print "The bikes that they can afford are:"
    for bike in affordable_bikes:
        print bike

for model in bike_shop.inventory:
    print "We currently have %s of the %s bike model" % (bike_shop.inventory[model], model)


for cust in customers:

    while True:
        purchase = random.sample(customer_bikes[cust.name], 1)
        if bike_shop.inventory [purchase[0]] != 0:
            break
    price = bike_shop.bike_prices[purchase[0]]
    profit += price - bike_catalog[purchase[0]][1]
    bike_shop.inventory[purchase[0]] -= 1

    print "%s has purchased a %s bike which costs %s dollars " %(cust.name, purchase[0],price)
    print "They have %s dollars left over" % (cust.budget - price)
    print "The %s bike shop has %s %s bikes left in their inventory" % (bike_shop.name, bike_shop.inventory[purchase[0]], purchase[0])

print "They made a profit of %s out of these bike sales" % (profit)
#for model in bike_shop.inventory:
 #   print "We currently have %s of the %s bike model" % (bike_shop.inventory[model], model)





def main():
    pass

if __name__ == '__main__':
    main()
