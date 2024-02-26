import sys
from fonctions_annexes import *
import re

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 1) or is_num(arguments[0])):
    error_case()

#Function that make uppercase the first letter of each word
def make_first_letter_upper(sentence):
    stringRes = ""

    cptLen = 0
    #Loop from 0 to the end of the string
    for i in range(0,len(sentence)):
        charTmp = sentence[i]

        if (charTmp.isalpha() or re.match('[^\w\s]+', charTmp) != None):  #Condition to be in a word
            if (cptLen == 0):                   #If its the index of the first char -> toUpper
                stringRes += charTmp.upper()
                cptLen += 1
            else:
                stringRes += charTmp.lower()    #Else its normal so lower
                cptLen += 1
        else:  #We are not in a word
            cptLen = 0                          #Reset the counter
            stringRes += charTmp                #Also add the char to the res

    return stringRes


sentence = arguments[0]
#Display the result
print(make_first_letter_upper(sentence))
