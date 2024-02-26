import sys
from fonctions_annexes import *

#Get the array of args
arguments = sys.argv[1:]

#Check if the arguments are OK
if (is_args_len_inf(arguments, 2) or is_args_all_num(arguments)):
    error_case()

#By the same algo than bubble sort
def tri_ascii(tab):
    n = len(tab)

    #Explore the list
    for i in range(n):
        for j in range(0, n-i-1): #For the index that goes until the pre ultime value
            if (ord(tab[j][0]) > ord(tab[j+1][0])): #get th ord for the ascii order
                tab[j], tab[j+1] = tab[j+1], tab[j] #Replace the values in the tab

    return tab

#Display the result
print(tri_ascii(arguments))
