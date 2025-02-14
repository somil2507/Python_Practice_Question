def find_least_positive_missing_number():

    arr = [1,-1,3,7,8,0,2,5,-6]

    missing_array = []
    positive_array = []

    for i in arr:
        if i >=1 :
            missing_array.append(i)

    missing_array.sort()
    print(missing_array)  

    for i in range(1, missing_array[-1]):
        if i not in missing_array:
            positive_array.append(i)


    print(positive_array[0])         
            

find_least_positive_missing_number()         