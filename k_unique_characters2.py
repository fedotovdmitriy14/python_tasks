def k_unique_characters(strparam):
    k = int(strparam[0])
    strParam_without_k = strparam[1:]
    result = []
    new_str = ''
    check_list = []

    while len(strParam_without_k) > k:
        for i in strParam_without_k:
            if i not in check_list and len(check_list) != k:
                check_list.append(i)
                new_str += i
            elif i not in check_list:
                break
            elif i in check_list:
                new_str += i 
        result.append(new_str)
        strParam_without_k = strParam_without_k[1:]
        check_list = []
        new_str = ''
    
    return max(result, key=len)

    
    

print(k_unique_characters('3abcebdbeaaafa'))
print(k_unique_characters('3aabacbebebe'))
print(k_unique_characters('2aabbcbbbadef'))


# a_list = ["a_string", "the_longest_string", "string"]
# longest_string = max(a_list, key=len)
# print(longest_string)