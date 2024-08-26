def frequent_words():
    str1 = "Hello my name is Somil and my house is in Thane"

    lst1 = str1.split()

    dict1 = {}

    for i in lst1:
        if i not in dict1.keys():
            dict1[i] = 0
        dict1[i] = dict1[i] + 1

    print(dict1) 

frequent_words()    



