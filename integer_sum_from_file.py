def add_integer_from_file():

    total = 0

    with open('my_script.txt', 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.isdigit():
                    total = total + int(word)

    print(total) 

add_integer_from_file()                   
