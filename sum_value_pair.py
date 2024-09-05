def find_sum_value_pair():

    arr = [5,7,4,3,9,8,19,21]
    sum = 17

    arr.sort()

    left = 0
    right = len(arr) - 1

    while(left<right):

        if arr[left] + arr[right] > sum:
            right = right-1
        elif arr[left] + arr[right] < sum:
            left = left + 1
        elif arr[left] + arr[right] == sum:
            print("Pairs are : ", arr[left], " ", arr[right])
            left = left + 1
            right = right - 1

find_sum_value_pair()                    