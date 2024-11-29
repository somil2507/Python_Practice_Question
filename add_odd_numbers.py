def add_odd_numbers():

    a = 1
    total = 0

    # while a <= 50:
    #     total = total + a
    #     a = a + 2

    while a <= 50:
        if a % 2 != 0:
            total = total + a
        a = a + 1    

    print(total)

add_odd_numbers()        