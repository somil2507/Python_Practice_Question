def find_missing_A_find_repeat_B():

    arr = [13, 5, 6, 1, 2, 14, 3, 9, 8, 11, 4, 10, 12, 14]
    N = 14

    A = 0
    B = 0

    for i in range(1,N+1):
        if i not in arr:
            A = i

    print("Missing A : ", A) 

    for i in range(1,N+1):
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:
                B = arr[j]

    print("Repeat B : ", B)                   

find_missing_A_find_repeat_B()        