from gettext import find


def find_missing_numbers():

    arr = [1,2,3,4,6,7,10]

    missing_array = []

    arr.sort()

    for i in range(arr[0], arr[-1]):
        if i not in arr:
            missing_array.append(i)

    print(missing_array) 

find_missing_numbers()            