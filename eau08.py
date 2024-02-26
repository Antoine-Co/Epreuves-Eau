import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 1)):
    error_case()

string1 = arguments[0]
#Display the result
print(is_num(string1))
