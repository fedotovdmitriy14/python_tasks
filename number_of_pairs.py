# Winter is coming, you must prepare your ski holidays. The objective of
# this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.
#
# Given an array describing the color of each glove, return the number of pairs
# you can constitute, assuming that only gloves of the same color can form pairs.


# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)
#
# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

from collections import defaultdict


def number_of_pairs(gloves):
    number_of_colors = defaultdict(int)
    result = 0
    for color in gloves:
        number_of_colors[color] += 1
        if number_of_colors[color] == 2:
            result += 1
            number_of_colors[color] = 0
    return result

print(number_of_pairs(["red", "green", "red", "blue", "blue"]))



