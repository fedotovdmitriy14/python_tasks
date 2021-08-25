def games_results():
    number = int(input())
    d = {}
    for i in range(number):
        a = input().split(';')
        if a[0] not in d:
            d[a[0]] = [0, 0, 0, 0, 0]
        if a[2] not in d:
            d[a[2]] = [0, 0, 0, 0, 0]
        d[a[0]][0] += 1
        d[a[2]][0] += 1
        # print(int(a[1]) > int(a[3]))
        if int(a[1]) > int(a[3]):
            d[a[0]][1] += 1
            d[a[0]][4] += 3
            d[a[2]][3] += 1
        if int(a[1]) < int(a[3]):
            d[a[2]][1] += 1
            d[a[2]][4] += 3
            d[a[0]][3] += 1
        if int(a[1]) == int(a[3]):
            d[a[0]][3] += 1
            d[a[2]][3] += 1
            d[a[0]][2] += 1
            d[a[2]][2] += 1

    for q, w in d.items():
        print((q+':'), *w, end='\n')

games_results()