import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check for bad arguments
if(is_args_len_sup(arguments, 0)):
    error_case("Pas besoin d'arguments !")

#Return an array with combination of 3 numbers by ascending order
def make_array_combination():
    #Init an array to put values
    tab = []

    #Triple loop to get i j k from 0 to 9
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if(i < j and j< k): #Ascending order required : i < j < k
                    tab.append(str(i) + str(j) + str(k))

    return tab

#Display the result
print_list_to_string(make_array_combination())
