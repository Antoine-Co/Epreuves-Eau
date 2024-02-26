import sys
from fonctions_annexes import *

#Get the array of args
arguments = sys.argv[1:]

#Check if the arguments are OK
if (is_args_len_inf(arguments, 2) or not is_args_all_num(arguments)):
    error_case()

#Function to sort by the algo of selection
def tri_select(list):
    n = len(list)

    for i in range(0, n-2):
        min = i
        for j in range(i+1, n):
            if(list[j] < list[min]):
                min = j
        if (min != i):
            list[i], list[min] = list[min], list[i]
    return list

#Return array with int
def array_to_int(arguments):
    tabNum = []
    for arg in arguments:
        tabNum.append(int(arg))
    return tabNum

#Display the result
print(tri_select(array_to_int(arguments)))
