def find_missing_numbers():

    arr = [1,2,3,4,6,7,10]
    new_arr = []

    for i in range(arr[0], arr[-1]): 
        if i not in arr:
            new_arr.append(i)
    print(new_arr)


find_missing_numbers()