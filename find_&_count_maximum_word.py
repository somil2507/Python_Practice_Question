def count_maximum_word_in_a_sentence():

    str = "Hello how are you Vegeta"

    max_word = ""
    max_length = 0

    lst = str.split()

    for i in lst:
        if len(i) > max_length:
            max_word = i
            max_length = len(max_word)

    print("Max word : ", max_word)
    print("Max Length : ", max_length)         

count_maximum_word_in_a_sentence()    