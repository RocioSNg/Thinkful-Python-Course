#-------------------------------------------------------------------------------
# Name:        Pirate Bartender
# Purpose:
#
# Author:      Rocio Ng
# Created:     07/10/2014
#-------------------------------------------------------------------------------

import random

def main():
    print "Ahoy matey! Let me make the perfect drink for ye!!!"
    pirate_questions()
    glass = pirate_drink()
    print "I will make your drink with: "
    for ingredient in glass:
        print ingredient
    while True:
        if raw_input("Would you like to order another drink? ").lower() in ('y','yes'):
            pirate_questions()
            glass = pirate_drink()
            print "I will make your drink with: "
            for ingredient in glass:
                print ingredient
        else:
            break

#----Dictionaries-----#

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Arrrr ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Arrrrr ye one for a fruity finish? "
            }

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

answers = {"strong": False, "salty": False, "bitter": False, "sweet":False, "fruity" : False}

#--------------Functions----------#

def pirate_questions():
    ''' Asks question corresponding to each drink type(key) in the questions dictionary
        and gather repsonses in the answers dictionary '''
    for key in questions:
        if raw_input(questions[key]).lower() in ('y','yes'):
            answers[key] = True
    return answers

def pirate_drink():
    '''If answers to any drink attributes are true in the answers list, it will
    choose an ingredient from the ingredients dictionary and add it to the drink'''
    arr_drink = []
    for key in answers:
        if answers[key] == True:
            arr_drink += [random.choice(ingredients[key])]
    if len(arr_drink) == 0:
        print "I can't make ye a drink without no ingredients!"
    return arr_drink

if __name__ == '__main__':
   main()
