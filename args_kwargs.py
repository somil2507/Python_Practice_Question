#Args

def person(name, *data_args):

    # print(name)
    # print(data_args)

    for i in data_args:
        print(i)

person("somil", "thane", 27, 782935)    

#Kwargs

def person(name, **data_kwargs):

    # print(name)
    # print(data_kwargs)

    for i,j in data_kwargs.items():
        print(i, j)

person("somil", city="mumbai", age=27, mobile=782935)    