#-------------------------------------------------------------------------------
# Name:        Pirate Bartender
# Purpose:
#
# Author:      Rocio Ng
# Created:     07/10/2014
#-------------------------------------------------------------------------------

#----Questions dictionary-----#

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
            }

answers = {"strong": False, "salty": False, "bitter": False, "sweet":False, "fruity" : False}

def pirate_questions():
    for key in questions:
        if raw_input(questions[key]) in ('y','Y','Yes', 'yes'):
            answers[key] = True
    print answers

if __name__ == '__main__':
    pirate_questions()
