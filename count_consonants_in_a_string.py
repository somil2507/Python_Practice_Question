from itertools import count


def count_consonants_in_a_string():

    vowels = ['a', 'e', 'i', 'o', 'u']

    count = 0

    string1 = input("Enter a String: ", ).lower()

    for i in string1:
        if i not in vowels:
            count = count + 1

    print(count) 

count_consonants_in_a_string()           