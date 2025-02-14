from itertools import count


def prime_notprime():

    num = int(input("Enter a Number : ", ))
    count = 0

    if num > 1:
        for i in range(1,num+1):
            if num%i==0:
                count = count + 1 
        if count == 2:
            print("Prime Number")

        else:
            print("Not a Prime Number")       

    else:
        print("Please enter a valid number greater than 1.")


prime_notprime()