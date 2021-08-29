# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

# import re

# def array_diff(a, b):
#     a_str = ",".join(str(item) for item in a)
#     result = []
#     for i in b:
#         # while re.findall(rf"\b(?=\w){str(i)}\b(?!\w)", a_str):
#         while re.findall(str(i), a_str):
#             a_str = a_str.replace(str(i), "")
#     a = a_str.split(',')
#     # for i, item in enumerate(a):
#     #     if item == '':
#     #         del a[i]
#     for i in a:
#         if i != '':
#             result.append(int(i))
#     return result

def array_diff(a, b): 
    result = []
    res_dict = {number:1 for number in b}
    for i in a:
        if i not in res_dict:
            result.append(i) 
    return result




print(array_diff([1,-2,2,2,3],[2, -2]))
# == [1,3]