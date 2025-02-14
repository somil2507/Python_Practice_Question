from itertools import count


def count_vowels_from_string():

    vowels = ['a', 'e', 'o', 'i', 'u']

    string1 = input("Enter a string : ", ).lower()

    count = 0

    for i in string1:
        if i in vowels:
            count = count + 1

    print(count)

count_vowels_from_string()            