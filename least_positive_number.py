def check_least_positive():

    arr = [1,-1,3,7,8,0,2,5,-6]

    least_positive = 0

    new_arr = []

    for i in arr:
        if i > 0:
            new_arr.append(i)
    print(new_arr)  

    new_arr.sort()

    least_positive = new_arr[0]

    print(least_positive)  


check_least_positive()    