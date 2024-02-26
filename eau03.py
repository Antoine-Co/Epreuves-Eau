import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check for bad arguments
if(is_args_len_diff(arguments, 1) or not is_num(arguments[0])):
    error_case("Donnez un argument entier !")

#Function fibonacci that return the number associated to the position given
def fibonacci(position):
    if (position == 0):
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2) #Recursivity from the formula of fibonacci

#Display result
print(fibonacci(int(arguments[0])))
