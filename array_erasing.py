# Task
# You are given an sequence of zeros and ones. With each operation you are allowed to remove consecutive equal elements, however you may only remove single elements if no more groups of consective elements remain. How many operations will it take to remove all of the elements from the given sequence?

# Example
# For arr = [0, 1, 1, 1, 0], the result should be 2.

# It can be cleared in two steps:

# [0, 1, 1, 1, 0] -> [0, 0] -> [].

# For arr = [0, 1, 0, 0, 0], the result should be 3.

# It can be cleared in three steps:

# [0, 1, 0, 0, 0] -> [0, 1] -> [0] -> []

# Note that you can not remove 1 at the first step, because you cannot remove just one element while there are still groups of consective elements (see the rule above ^_^)

# Input
# A list lst of 0s and 1s.
# 1 <= len(lst) <= 100

# Output
# The minimum number (integer) of operations.



def array_erasing(lst):
    # result = 0
    # while len(lst) != 0:
    #     for i in range(len(lst)-1):
    #         if lst[i] == lst[i+1]:
    #             print('found')
    #             del lst[i]
    #             return lst

    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            for j in range(i, len(lst)):
                if lst[j] != lst[j+1]:
                    

    


print(array_erasing([0, 1, 1, 1, 0]))