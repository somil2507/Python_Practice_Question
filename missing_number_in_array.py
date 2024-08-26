def find_missing_number_in_array():
    arr1 = [1,2,3,5,6,7]

    n = arr1[-1]
    total = n*(n+1) // 2

    array_sum = sum(arr1)

    missing_number = total - array_sum

    print(missing_number)

find_missing_number_in_array()    