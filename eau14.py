import sys
from fonctions_annexes import *

#Get the array of args
arguments = sys.argv[1:]

#Check if the arguments are OK
if (is_args_len_inf(arguments, 2) or is_args_all_num(arguments)):
    error_case()
