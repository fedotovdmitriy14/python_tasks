def revrot(strng, sz):
    if sz <= 0 or strng == '':
        return ""
    else:
        result = list((strng[i:i+sz] for i in range(0, len(strng), sz)))            
        result2 = []
        for i in result:                                   
            if len(i) % sz == 0:
                sum = 0
                for n in range(len(i)):
                    sum += int(i[n])**2
                print(sum)
                if sum % 2 == 0:
                    result2.append(i[::-1])
                else:
                    result2.append(i[1:]+i[0])

    return ''.join((str(item) for item in result2))                                        


print(revrot("123456987654", 6))
print(revrot("66443875", 4))
print(revrot('', 1))



# revrot("123456987654", 6) --> "234561876549"