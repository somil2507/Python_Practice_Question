def count_consonants():

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    string_input = input("Enter a String : ", ).lower()

    new_string = []

    
    for word in string_input:
        if word.isalpha():
            new_string.append(word)

    for i in new_string:
        if i not in vowels:
            count = count + 1

    print("Total Consonants are : ", count)


count_consonants()
