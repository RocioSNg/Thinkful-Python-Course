#-------------------------------------------------------------------------------
# Name:        Fizz Buzz v2
# Author:      Rocio Ng
#-------------------------------------------------------------------------------

import sys

#define Fizz Buzz function
def fizz_buzz(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print "fizz buzz"
        elif num % 3 == 0:
            print "fizz"
        elif num % 5 == 0:
            print "buzz"
        else:
            print num

if len(sys.argv) == 2:
    print "Fizz buzz counting up to {}" .format(sys.argv[1])
    fizz_buzz(int(sys.argv[1]))

elif len(sys.argv) == 1:
    number = raw_input("Please enter a number")
    #if type(int(number))!= int:
        #number = raw_input("Please enter a NUMBER")
    fizz_buzz(int(number))