from itertools import count


def print_prime_numbers_for_given_range():

    start = 100
    end = 150

    print("Prime numbers are :")

    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break

            else:
                print(num)   

print_prime_numbers_for_given_range()                     