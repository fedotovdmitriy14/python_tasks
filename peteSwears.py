# Так пытался я:


# def pete_talk(speech):
#     speech_list = speech.split()
#     final_result = []
#     for word in speech_list:
#         if len(word) > 2:
#             new_word = ""
#             for index, letter in enumerate(word):
#                 if index != 0 and index != len(word)-1:
#                     new_word += "*"
#                 else:
#                     new_word += letter
#             final_result.append(new_word)

    
#     return " ".join(final_result)

# speech = "Hello, you fucking asshole!"
# print(pete_talk(speech))



# А вот так можно было:

def pete_talk(speech,ok=None):
    if ok == None: ok = []
    ok = [wrd.lower() for wrd in ok]
    speech = speech.lower()
    res = []
    for wrd in speech.split():
        sign = ''
        if not wrd[-1].isalpha():
            wrd, sign = wrd[:-1], wrd[-1]
        if len(wrd) > 2 and wrd not in ok:
            res.append(wrd[0] + '*' * (len(wrd)-2) + wrd[-1] + sign)
        else:
            res.append(wrd + sign)
    for i, wrd in enumerate(res):
        if i == 0:
            res[i] = wrd[0].upper() + wrd[1:]
        else:
            if res[i-1][-1] in '.!?':
                res[i] = wrd[0].upper() + wrd[1:]
    return ' '.join(res)



        
word = 'Sveta!'
print(word[:-1])
res = [] 
sign = ''
if not word[-1].isalpha():
    word, sign = word[:-1], word[-1]
if len(word) > 2:
    res.append(word[0] + '*' * (len(word)-2) + word[-1] + sign)    
print(res)
      


