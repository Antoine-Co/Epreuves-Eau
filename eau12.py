import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the arguments are OK
if (is_args_len_inf(arguments, 2) or not is_args_all_num(arguments)):
    error_case()

#Function that sort a list with the bubble sort algo
def tri_bulle(tab):
    n = len(tab)

    #Explore the list
    for i in range(n):
        for j in range(0, n-i-1): #For the index that goes until the pre ultime value
            if (tab[j] > tab[j+1]):
                tab[j], tab[j+1] = tab[j+1], tab[j] #Replace the values in the tab

    return tab

#Return array with int
def array_to_int(arguments):
    tabNum = []
    for arg in arguments:
        tabNum.append(int(arg))
    return tabNum

#Display the result
print(tri_bulle(array_to_int(arguments)))
