def remove_duplicates():

    arr = [40,20,10,10,30,50,10]
    out_arr = []

    for i in arr:
        if i not in out_arr:
            out_arr.append(i)

    print(out_arr)

remove_duplicates()   