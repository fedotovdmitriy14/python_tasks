# Task:
# Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:
#
#
# I I I I  # each Pin has a Number:    7 8 9 10
#  I I I                                4 5 6
#   I I                                  2 3
#    I                                    1
#
# You will get an Array with Numbers, e.g.: [3,5,9] and remove them from the field like this:
#
#
# I I   I
#  I   I
#   I
#    I
#
# Return a string with the current field.
#
# Note that:
# You begin a new line with \n
# Each Line must be 7 chars long
# Fill the missing pins with a whitespace
# Have fun!

import re

def bowling_pins(arr):
    # full_field = 'I I I I\n I I I \n  I  I  \n   I   '
    full_field = '7 8 9 10\n 4 5 6 \n  2 3  \n   1   '

    for i in arr:
        i = str(i)
        full_field = re.sub(i + r'\b', ' ', full_field)
    full_field = re.sub(r'10', 'I', full_field)
    full_field = re.sub(r'\d', 'I', full_field)

    return full_field



print(bowling_pins([2, 3]))             #"I I I I\n I I I \n       \n   I   ")
print(bowling_pins([1, 2, 10]))          # "I I I  \n I I I \n    I  \n       ")
print(bowling_pins([1]))