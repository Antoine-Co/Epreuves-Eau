import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 1) or not is_args_all_alpha(arguments[0])):
    error_case()

#Set upperCase one letter on two in a string
def set_upper_one_on_two(string1):
    stringRes = ""
    #Explore the string for each char and putting uppercase 1 on 2
    for i in range(len(string1)):
        if (i%2 == 0):
            stringRes += string1[i].upper()
        else:
            stringRes += string1[i].lower()
    return stringRes

#Display the result
print(set_upper_one_on_two(arguments[0]))
