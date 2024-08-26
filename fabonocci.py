def fabonocci_series():

    num = int(input("Enter a number : ", ))

    a = 0
    b = 1

    if num < 0:
        print("Enter non decimal positve number greater than 0")

    elif num == 1:
        print(a)

    else:
        print(a)
        print(b)
        
        for i in range(2,num):
            c = a+b
            a = b
            b = c

            print(c)

fabonocci_series()                    
        