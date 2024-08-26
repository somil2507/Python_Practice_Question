def substring():

    str1 = "hello welcome to ambikapur"

    lst = str1.split()

    sub_str = "mumbai"

    if sub_str in lst:
        print(sub_str, " is a substring")
    else:
        print(sub_str, " is not a substring")    

substring()    