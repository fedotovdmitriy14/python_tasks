# Task
# You will be given a string of English digits "stuck" together, like this:
#
# "zeronineoneoneeighttwoseventhreesixfourtwofive"
#
# Your task is to split the string into separate digits:
#
# "zero nine one one eight two seven three six four two five"


def uncollapse(digits):
    digit_list = ['zero', 'one', 'two', 'three', 'four',
                  'five', 'six', 'seven', 'eight', 'nine']

    word = ''
    result = []
    for i in digits:
        word += i
        if len(word) >= 3:
            if word in digit_list:
                result.append(word)
                word = ''

    return " ".join(result)


print(uncollapse("ninethreesixthree"))