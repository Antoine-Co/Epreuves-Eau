import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 2)):
    error_case()

#Return the index of the first element == element in the list
def index_in_list(arguments, stringToFind):
    for elt in arguments:               #Iterate on the list
        if (stringToFind == elt):
            return arguments.index(elt) #Return the index if string1 is found in the list
    return -1

#Get list arguments less the string searched
stringToFind = arguments.pop()

#Display the result
print(index_in_list(arguments, stringToFind))
