from unittest import result


def adding_two_list():

    l1 = [2,3,4]
    l2 = [4,3,2]

    result = []

    for i in range(0, len(l1)):

        result.append(l1[i] + l2[i])

    print(result)    

adding_two_list()            