# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


import string

def pig_it(text):
    text_list = text.split()
    punct = string.punctuation
    result = []
    for i in text_list:
        if i not in punct:
            i = i[1::] + i[0] + 'ay'
            result.append(i)
        else:
            result.append(i)

    return " ".join(result)



print(pig_it('Pig latin is cool'))