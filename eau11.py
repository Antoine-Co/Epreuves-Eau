import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_inf(arguments, 2) or not is_args_all_num(arguments)):
    error_case()

#Return the minimum of the absolute substraction between 2 nb in the list
def min_diff_abs(list):
    listDiff = []

    #Loop to have the index
    for i in range(len(list)):
        eltTmp = list[i]

        for elt in list: #Loop 2 to dont substract one element by himself
            if(list.index(elt) != list.index(eltTmp)):
                listDiff.append(abs(abs(int(eltTmp)) - abs(int(elt)))) #absolute substraction

    return take_smallest(listDiff)

#Keeping the value the smallest
def take_smallest(listNumber):
    min = listNumber[0]
    for elt in listNumber[1:]:
        if(elt < min):
            min = elt
    return min

#Display the result
print(min_diff_abs(arguments))
