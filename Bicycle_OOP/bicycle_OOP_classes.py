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
        self.model_name = model_name #name of the model
        self.weight = weight  #in pounds
        self.production_cost = production_cost  #how much it costs to make each bike of that model

class Bike_Shop(object):

    def __init__(self, name, model_list):
        self.name = name
        self.model_list = model_list    #list of models of bikes that the store has in stock

    def bike_inventory(self,model_list):
        '''creates a list of instances of the bike class'''
        inventory = []
        for item in model_list:
            #item = "Schwinn"
            bike = Bicycle(item, bike_catalog[item][0],bike_catalog[item][1])  #grabs the info from the bike catalog to make instances of each bike
            inventory.append(bike)   #adds each bike to the inventory
        return inventory
    def bike_sell_price (self,inventory):
        '''determines selling price for each bike
        which is 20% higher than production costs'''
        bike_store_prices= {}
        for item in inventory:
            bike_store_prices[item.model_name] = item.production_cost + (item.production_cost*.2)
        return bike_store_prices

class Customer(object):
    can_buy_bike = True
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

bike_catalog = {"Schwinn":[19,100],"Trek":[18,400],"Specialized": [15,900],"Cannondale":[19,200],"Giant":[18,450],"Fuji":[20,50]}  #models with weights and production costs
bike_shop1_models = ["Schwinn", "Trek", "Specialized","Cannondale", "Giant","Fuji"]  #List of models that bike shop1 has
bike_shop1_inventory = {"Shwinn": 3, "Trek": 1, "Specialized":1, "Cannondale":1, "Giant":1, "Fuji": 1}

Bike_Shop1 = Bike_Shop("On Two Wheels", bike_shop1_models)
inventory = Bike_Shop1.bike_inventory(bike_shop1_models)
for bike in inventory:
    print bike.model_name
bike_prices = Bike_Shop1.bike_sell_price(inventory)
print bike_prices


print "Welcome to the bicycle shop called: %s" % Bike_Shop1.name



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

print "The %  store has the following left in stock:" % Bike_Shop1.name
for bike in bike_shop1_inventory:
    print " %s of the %s model left" % ( bike_shop1_inventory[bike], bike)

bike1 = Bicycle("Schwinn", 19, 300)
bike2 = Bicycle("Trek", 18, 500)
bike3 = Bicycle("Specialized", 15, 600)
bike4 = Bicycle("Cannondale", 19, 200)
bike5 = Bicycle("Giant", 18, 550)
bike6 = Bicycle("Fuji", 20, 250)





def main():
    pass

if __name__ == '__main__':
    main()
