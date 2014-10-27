#-------------------------------------------------------------------------------
# Name:        Bicycle Industry Classes
# Purpose:  Define classes for Bicycle Industry Modelling Project
#
# Author:      Rocio Ng
#
# Created:     16/10/2014
#-------------------------------------------------------------------------------


class Bicycle(object):
    def __init__(self, model_name, weight, production_cost):
        self.model_name = model_name
        self.weight = weight  #in pounds
        self.production_cost = production_cost


class Bike_Shop(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory    #dictionary of models of bikes and their inventory numbers
        self.bikes = bike_list(self, inventory)

    def bike_list(self,inventory):
        bikes = []
        for key in inventory:
            #item = "Schwinn"
            bike = Bicycle(key, bike_catalog[key][0],bike_catalog[key][1])  #grabs the info from the bike catalog to make instances of each bike
            bike_list.append(bike)   #adds each bike to the inventory
        return bikes
        #return inventory ## not necessary
        #self.bike_list = bike_list

    def bike_sell_price (self,bike_list):
        '''determines selling price for each bike
        which is 20% higher than production costs'''
        bike_store_prices= {}
        for item in bike_list:
            bike_store_prices[item.model_name] = item.production_cost + (item.production_cost*.2)
        #return bike_store_prices
        self.bike_prices = bike_store_prices

class Customer(object):
    can_buy_bike = True
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

bike_catalog = {"Schwinn":[19,100],"Trek":[18,400],"Specialized": [15,900],"Cannondale":[19,200],"Giant":[18,450],"Fuji":[20,50]}  #models with weights and production costs
#bike_shop1_models = ["Schwinn", "Trek", "Specialized","Cannondale", "Giant","Fuji"]  #List of models that bike shop1 has
bike_shop1_inventory = {"Shwinn": 3, "Trek": 1, "Specialized":4, "Cannondale":1, "Giant":2, "Fuji": 1}


Bike_Shop1 = Bike_Shop("On Two Wheels", bike_shop1_inventory)
#inventory = Bike_Shop1.bike_inventory(bike_shop1_models)
#for bike in inventory:
 #   print bike.model_name
print Bike_Shop1.bike_list
#print bike_prices


print "Welcome to the bicycle shop called: %s" % Bike_Shop1.name
for key in Bike_Shop1.inventory:
    print "We currently have %s of the %s bike model" % ( Bike_Shop1.inventory[key], key)


#------Customers-----#
cust1 = Customer("Finn", 200)
cust2 = Customer("Jake", 500)
cust3 = Customer("Marceline", 1000)

customers = [cust1,cust2, cust3]  #List with all the customers

for cust in customers:
    print "The name of the customer is: %s" % cust.name
    afforable_bikes = []

    for bike in bike_prices:
        if bike_prices[bike] <= cust.budget:
            afforable_bikes.append(bike)
    print "The bikes that they can afford are:"
    for bike in afforable_bikes:
        print bike

#print "The %  store has the following left in stock:" % Bike_Shop1.name
#for bike in bike_shop1_inventory:
   # print " %s of the %s model left" % ( bike_shop1_inventory[bike], bike)




def main():
    pass

if __name__ == '__main__':
    main()
