def count_frequency():

    str = "hello welcome to city of dreams mumbai city"

    lst = str.split()

    d = {}

    for i in lst:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1

    print(d)

count_frequency()    