import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check for bad arguments
if(is_args_len_sup(arguments, 0)):
    error_case("Pas besoin d'arguments !")

#Return an array with combination of 2 numbers of 2 digits by ascending order
def make_array():
    #Init an array to put the values
    tab = []

    #Quad loop to get i j k l from 0 to 9
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    if (int(str(i)+str(j)) < int(str(k)+str(l))):  #Condition ascending order ij > kl
                        tab.append(str(i) + str(j) + " " + str(k) + str(l))

    return tab

#Display the result
print_list_to_string(make_array())
