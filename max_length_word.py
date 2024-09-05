def max_length_word_in_sentence():

    str = "hello my name is kakrot"

    max_word = ""
    max_len = 0

    lst = str.split()

    for i in lst:
        if len(i) > max_len:
            max_word = i
            max_len = len(max_word)

    print(max_word)
    print(max_len)


max_length_word_in_sentence()
   