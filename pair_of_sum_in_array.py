from turtle import left, right


def find_pair_of_sum():

    arr1 = [5,7,4,3,9,8,19,21]
    sum_value = 17

    arr1.sort()
    left = 0
    right = len(arr1) - 1

    while(left<=right):

        if (arr1[left]+arr1[right] > sum_value):
            right = right-1
        elif (arr1[left]+arr1[right] < sum_value):
            left = left + 1
        elif (arr1[left]+arr1[right] == sum_value):
            print("The pairs are : ", arr1[left], "& ", arr1[right]) 
            right = right-1
            left = left+1  

find_pair_of_sum()                 