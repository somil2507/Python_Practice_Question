def dictonary_to_tuples():

    d = {'one': 1, 'two': 2, 'three': 3}

    l1 = []
    l2 = []

    for i in d.keys():
        l1.append(i)
    for j in d.values():
        l2.append(j)    

    t1 = tuple(l1)
    t2 = tuple(l2)

    print(t1)
    print(t2)  

dictonary_to_tuples()        