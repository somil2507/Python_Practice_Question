def remove_white_spaces_from_a_string():

    word = "c o d e"

    word_lst = list(word)
    word_lst_1 = []
    output = ""
    
    print(word_lst)

    for i in word_lst:
        if i.isalpha():
            word_lst_1.append(i)

    output = ''.join(word_lst_1)        

    print(word_lst_1)    
    print(output)    



remove_white_spaces_from_a_string()    