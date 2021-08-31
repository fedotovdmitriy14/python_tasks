# For a given string s find the character c (or C) with longest consecutive repetition and return:

# (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

# For empty string return:

# ('', 0)
# Happy coding! :)



def longest_repetition(chars):
    if chars == '':
        return ('', 0)
    sorted_list = []
    final = []
    length = 1
    for i in range(len(chars)):
        try:
            if chars[i] == chars[i+1]:
                length += 1
            else:
                sorted_list.append(chars[i])
                sorted_list.append(length)
                length = 1
        except IndexError:
            sorted_list.append(chars[i])
            sorted_list.append(length)
    for i in range(1, len(sorted_list), 2):
        final.append(sorted_list[i])
    max_length = max(final)
    for i in range(1, len(sorted_list), 2):
        if sorted_list[i] == max_length:
            return sorted_list[i-1], sorted_list[i]



        

print(longest_repetition("aaaabbbbb"))