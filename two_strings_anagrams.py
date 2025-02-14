def compare_two_strings_are_anagrams():

    str1 = "listen"
    str2 = "silent"

    l1 = list(str1)
    l2 = list(str2) 

    if l1.sort() == l2.sort():
        print("True")

    else:
        print("False")    

compare_two_strings_are_anagrams()        