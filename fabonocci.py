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


def fab_series(n):

  l1 = [0,1]

  for i in range(2,n):

    l1.append(l1[i-1] + l1[i-2])

  return l1[:n]

fab_series(5)  
