# Encrypt this!
#
# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
#
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.


def encrypt_this(text):
    result = []
    for word in text.split():
        if len(word) == 1:
            result.append(str(ord(word[0])))
        else:
            word = list(word)
            word[1], word[-1] = word[-1], word[1]
            word[0] = str(ord(word[0]))
            result.append(''.join(word))
    return " ".join(result)

print(encrypt_this("hello world"))
print(encrypt_this(""))
print(encrypt_this("A wise old owl lived in an oak"))