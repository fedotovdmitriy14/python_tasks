import re

def k_unique_characters(strparam):
    k = int(strparam[0])
    strParam_without_k = strparam[1:]
    result_dct = {}
    new_str = ''
    check_list = []

    while len(strParam_without_k) > k:
        for i in strParam_without_k:
            if i not in check_list and len(check_list) != k:
                check_list.append(i)
                new_str += i
            elif i in check_list:
                new_str += i
        result_dct[len(new_str)] = new_str
        strParam_without_k = strParam_without_k.replace(check_list[0], '')
        check_list = []
        new_str = ''
    
    

    return result_dct
    
    

print(k_unique_characters('3abcebdbeaaafa'))
print(k_unique_characters('3aabacbebebe'))