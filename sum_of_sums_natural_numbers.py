def sum_of_sums():

    n = int(input("enter value of n : ",))

    k = 0

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            k = k + j

    print("sum of sums is : ", k)

sum_of_sums()            