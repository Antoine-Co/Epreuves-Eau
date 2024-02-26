import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 2) or not is_num(arguments[0]) or not is_num(arguments[1])):
    error_case()

#Return the array of values between int1 and int2
def values_between(number1, number2):
    tab = []
    if (number1 < number2):
        while(number1 != number2):
            tab.append(number1)
            number1 += 1
    else:
        if(number1 > number2):
            while number1 != number2:
                tab.append(number2)
                number2 += 1
    return tab

#Get values
number1 = int(arguments[0])
number2 = int(arguments[1])

#Display the results
print_list_to_string(values_between(number1, number2))
