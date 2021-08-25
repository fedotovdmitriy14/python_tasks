import re

def group_by_commas(n):
    result = ''
    n = str(n)
    for number in n[::-1]:
        if len("".join(re.findall(r'[A-Z0-9a-z]', result)))   % 3 == 0 and len(result) != 0:
            result += ',' + number
        else: 
            result += number
    return result[::-1]
    


print(group_by_commas(1000000))