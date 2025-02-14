def assign_user():
    arr = [37, 43, 44, 23, 71, 7, 92, 87, 17, 59, 9, 79, 22, 54, 13, 58, 72, 32, 4, 82, 49, 40, 45, 94, 65, 56, 99, 86, 77, 41, 47, 2, 75, 96, 28, 83, 64, 46]

    print("Total elements in arr:", len(arr))

    a = []
    b = []
    c = []
    d = []

    for i in arr:
        if len(a) < 10:
            a.append(i)
        elif len(b) < 10:
            b.append(i)
        elif len(c) < 10:
            c.append(i)
        elif len(d) < 10:
            d.append(i)

    print("Array a:", a)
    print("Array b:", b)
    print("Array c:", c)
    print("Array d:", d)

assign_user()