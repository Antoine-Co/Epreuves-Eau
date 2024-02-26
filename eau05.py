import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 2) or not is_alpha(arguments[0]) or not is_alpha(arguments[1])):
    error_case()

#Function to know if string2 is contained into string1
def is_inside(string1, string2):
    if(string1[0] == string2[0] and len(string1) >= len(string2)): #If first char is equal and the lenght correspond
        if (string1[0:len(string2)] == string2):   #If from the letter in common the word appear in the first string : OK
            return True
        else:
            return False
    else:
        if(len(string1) > len(string2)):           #Check the lenght to find string2 in string1 -first letter
            return is_inside(string1[1:], string2) #Recursivity to check deeper in the string1
        else:
            return False                           #In others cases its not inside

#Get the values
string1 = arguments[0]
string2 = arguments[1]

#Display the result
print(is_inside(string1,string2))
