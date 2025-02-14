def generator_test():

    n = 1
    sq = 1

    while n <= 10:

        sq = n * n
        yield sq
        n = n + 1

square_values = generator_test()     

for i in square_values:
    print(i)
