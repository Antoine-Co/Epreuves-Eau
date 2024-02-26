import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check for bad arguments
if(is_args_len_inf(arguments, 2)):
    error_case("Donnez des arguments !")

#Return the reversed array of args
def make_reverse_args(args):
    listReverseArgs = []

    for arg in args[::-1]: #Backward  iteration loop
        listReverseArgs.append(arg)

    return listReverseArgs

#Display the result
print_list_by_line(make_reverse_args(arguments))
