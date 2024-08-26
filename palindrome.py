def check_palindrome():

    str1 = input("Enter a string : ", )

    reverse_str = str1[::-1]

    if str1 == reverse_str:
        print("Palindrome")

    else:
        print("Not Palindrome")    
check_palindrome()    