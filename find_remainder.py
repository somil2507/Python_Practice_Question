def find_remainder(x,y):

    if x < y:
        return x
    return find_remainder(x-y,y)

print(find_remainder(30,10))    
