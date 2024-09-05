def check_prime():

    num = 3
    count = 0

    if num > 1:
        for i in range(1,num+1):
            if num % i == 0:
                count = count + i

        if count == 2:
            print("Prime")

        else:
            print("Not Prime")            

check_prime()                    
