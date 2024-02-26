import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 1) or not is_num(arguments[0]) or int(arguments[0]) < 2):
    error_case("-1")

#Boolean function that return if a number is Prime
def is_prime(inputInt):
    #From 2 to the int because we already have it
    for i in range(2,inputInt - 1):
        if (inputInt%i == 0):      #Modulo to find ones == 0
            return False
        i += 1
    return True

def find_next_prime(inputInt):
    inputInt += 1                  #To have the next prime nb > arg
    while(not is_prime(inputInt)):  #While its not prime take the next
        inputInt += 1
    return inputInt

#Display the result
inputInt = int(arguments[0])
print(find_next_prime(inputInt))
