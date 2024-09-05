def find_repeat_and_smallest_number():

    arr = [2,2]
    N= 2


    repeat_number = []
    smallest_number = 0

    for i in range(1, N+1):
        if i == arr:
            repeat_number = i
    print("Repeating Number : ", i)

    for i in range(1, N+1):
        if i not in arr:
            smallest_number = i
    print("Smallest Number : ", smallest_number)      
           

find_repeat_and_smallest_number()            