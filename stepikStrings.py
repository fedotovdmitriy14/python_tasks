# s = "abababa"
# t = "aba"


# s = "abababa"
# t = "abc"

s = input()
t = input()

start = 0
finish = len(t)
result = 0

while finish <= len(s): 
    if s.startswith(t, start, finish):
        result += 1
        start += 1
        finish += 1
    else:
        start += 1
        finish += 1

print(result)