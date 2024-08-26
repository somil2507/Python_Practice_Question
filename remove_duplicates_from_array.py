from subprocess import list2cmdline


def remove_duplicate_from_sorted_array():

    arr1 = [1,1,1,2,2,3,3,4]

    unique_array = list(set(arr1))

    print(unique_array)
    n = len(unique_array)

    print(n)

remove_duplicate_from_sorted_array()    