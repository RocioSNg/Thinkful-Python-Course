#-------------------------------------------------------------------------------
# Name:        Bicycle Industry Classes
# Purpose:  Define classes for Bicycle Industry Modelling Project
#
# Author:      Rocio Ng
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
        self.bikes = self.bike_list(inventory)
        self.bike_prices = self.bike_sell_price(self.bikes)

    def bike_list(self,inventory):
        bikes = []
        for key in inventory:
            #item = "Schwinn"
            bike = Bicycle(key, bike_catalog[key][0],bike_catalog[key][1])  #grabs the info from the bike catalog to make instances of each bike
            bikes.append(bike)   #adds each bike to the inventory
        return bikes
        #return inventory ## not necessary
        #self.bike_list = bike_list

    def bike_sell_price (self,bike_list):
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




def main():
    pass

if __name__ == '__main__':
    main()
