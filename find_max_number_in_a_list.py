from time import process_time


def find_max_number_in_a_list():

    lst = [45,23,1,78,56,20]

    max_num = lst[0]

    for i in lst:
        if max_num < i:
            max_num = i

    print(max_num)

find_max_number_in_a_list()            