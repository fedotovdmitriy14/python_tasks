# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
#
# For each word:
#
# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces
#
# Examples
#
# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'

import re


def decipher_this(string):
    result = re.findall(r'\d+', string)
    for i in result:
        if i in string:
            string = string.replace(i, chr(int(i)))
    result = []
    for i in string.split():
        if len(i) > 2:
            i = list(i)
            i[1], i[-1] = i[-1], i[1]
            result.append("".join(i))
        else:
            result.append(i)
    return " ".join(result)


print(decipher_this('a'))
print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))