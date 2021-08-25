def longest_consec(strarr, k):
    new = []
    st = ''
    length = []
    if len(strarr) != 0 and k < len(strarr) and k >= 0:

        if k == 0:
            return ""


        while len(strarr) >= k:       
            st = ''        
            for i in range(k):
                st += strarr[i]
            new.append(st)
            new.append(len(st))
            length.append(len(st))
            strarr.pop(0)
        
        for i in range(len(new)):
            if new[i] == max(length):
                return new[i-1]

    else:
        return ""


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))

# new = ["zone", "abigail", "theta", "form", "libe", "zas"]
# print(new.pop(0))
# print(new)
