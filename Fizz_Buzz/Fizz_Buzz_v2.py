#-------------------------------------------------------------------------------
# Name:        Fizz Buzz v2
# Author:      Rocio Ng
#-------------------------------------------------------------------------------

import sys

#----Define Fizz Buzz function-----#

def fizz_buzz(n):
    '''Counts up to the number n.  Prints fizz if current number is divisible by 3,
    fuzz if divisble by 5 and fizz buzz if divisble by both.  Otherwise it prints
    the number
    '''
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:   #divisible by 3 and 5
            print "fizz buzz"
        elif num % 3 == 0:  #divisible by 3 only
            print "fizz"
        elif num % 5 == 0:  #divisible by 5 only
            print "buzz"
        else:
            print num

#--If user provides an input when running the program--#
if len(sys.argv) == 2:
    try:
        number = int(sys.argv[1])
    except ValueError:
        while True:
            try:
                number = raw_input("Please enter an integer : ")
                number = int(number)
                break
            except ValueError:
                print("Try Again")
    print "Fizz buzz counting up to " + str(number)
    fizz_buzz(number)

#----If user does not provide input----#
elif len(sys.argv) == 1:
    while True:
        #--Add Exception---#
        try:
            number = raw_input("Please enter an integer : ")
            number = int(number)
            break
        except ValueError:
            print ("I said enter an INTEGER...try again: ")
    print "Fizz buss counting up to " + str(number)
    fizz_buzz(number)
