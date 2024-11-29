def read_file():

    lst = []

    with open("my_script.txt", 'r') as file:

        for lines in file:
            words = lines.split()

            for word in words:
                if word.isdigit():
                    lst.append(int(word))

    print(lst)

read_file()                     