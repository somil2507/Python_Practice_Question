def find_minimum_number_in_a_list():

    lst = [34,28,45,62,7]

    min_num = lst[0]

    for i in lst:
        if min_num > i:
            min_num = i

    print(min_num) 

find_minimum_number_in_a_list()           