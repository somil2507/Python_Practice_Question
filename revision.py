from itertools import count
from multiprocessing.reduction import duplicate
from operator import le
from turtle import right


def find_least_positive_missing_integer():

    arr = [1,-1,3,7,8,0,2,5,-6]
    new_arr = []
    missing_least_integer = []

    for i in arr:
        if i > 0:
            new_arr.append(i)

    new_arr.sort()
    print(new_arr)

    for j in range(1, new_arr[-1]):
        if j not in new_arr:
            missing_least_integer.append(j)

    print(missing_least_integer[0])        
    

#find_least_positive_missing_integer()    
# 
# 

def find_missing_numbers():

    arr = [1,2,3,4,6,7,10]
    arr.sort()

    missing_arr = []

    for i in range(arr[0], arr[-1]):
        if i not in arr:
            missing_arr.append(i)

    print(missing_arr)

#find_missing_numbers()    

def find_max_word_and_length():

    str1 = "Hello how are you MSDhoni"

    max_word = ""
    max_length = 0

    lst = str1.split()

    for i in lst:
        if len(i) > max_length:

            max_word = i
            max_length = len(max_word)

    print(max_word)
    print(max_length)


#find_max_word_and_length()


def find_comman_letters():

    str1 = "NAINA"
    str2 = "REENA"

    st1 = set(str1)
    st2 = set(str2)

    comman = st1 & st2

    print(comman)

#find_comman_letters()    

def count_the_frequency_of_words():

    string1 = "mumbai city is a great city mumbai city is called the city of dreams"

    lst = string1.split()

    d = {}

    for i in lst:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1 

    print(d)

#count_the_frequency_of_words() 
# 

def add_only_odd_numbers():

    total = 0
    n = 1

    # for i in range(1, 51):
    #     if i % 2 != 0:
    #         total = total + i

    while n <= 50:
        total = total + n

        n = n + 2

    print(total)        

#add_only_odd_numbers() 
# 

def add_exponentials():

    total = 0

    n = int(input("Enter power range : ", ))

    for i in range(n+1):
        total = total + 2 ** i

    print(total)    

#add_exponentials()   
# 
def find_HCF():

    num1 = int(input("Enter first number : ", ))
    num2 = int(input("Enter second number : ", ))

    while num2 != 0:

        num1, num2 = num2, num1%num2

    print(num1)    

#find_HCF()

def print_first_ten_even_numbers():

    for i in range(20, 0, -2):
        print(i)

#print_first_ten_even_numbers()    

def pair_sum_values():

    arr = [5,7,4,3,9,8,19,21]

    sum_value = 17

    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:

        if arr[left] + arr[right] > sum_value:
            right = right - 1

        elif arr[left] + arr[right] < sum_value:
            left = left + 1

        elif arr[left] + arr[right] == sum_value:
            print("Pairs are : ", arr[left], "&",arr[right])

            left = left + 1
            right = right - 1

#pair_sum_values()        
# 

def find_missing_A():

    arr = []
    N = 14

    for i in range(1,N+1):
        if i not in arr:
            A = i

    print("Missing A : ", A) 

def find_repeating_B():

    arr = [13, 5, 6, 1, 2, 14, 3, 9, 8, 11, 4, 10, 12, 14]
    N = 14

    for i in range(1, N+1):
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:
                B = arr[j]

    print("Repeating B : ", B)             

# find_missing_A()
# find_repeating_B()   
# 

def assign_user():
    arr = [37, 43, 44, 23, 71, 7, 92, 87, 17, 59, 9, 79, 22, 54, 13, 58, 72, 32, 4, 82, 49, 40, 45, 94, 65, 56, 99, 86, 77, 41, 47, 2, 75, 96, 28, 83, 64, 46]

    print("Total elements in arr:", len(arr))

    a = []
    b = []
    c = []
    d = []

    for i in arr:
        if len(a) < 10:
            a.append(i)
        elif len(b) < 10:
            b.append(i)
        elif len(c) < 10:
            c.append(i)
        elif len(d) < 10:
            d.append(i)

    print("Array a:", a)
    print("Array b:", b)
    print("Array c:", c)
    print("Array d:", d)

#assign_user()

def check_prime_or_not():

    num = 6
    count = 1

    if num > 0:

        for i in range(1,num+1):
            if num % i == 0:
                count = count + 1
        if count == 2:
            print("Prime")
        else:
            print("Not Prime")

    else:
        print("Please enter number greater than 0")        

#check_prime_or_not()  

def prime_numbers_for_given_range():

    start = 100
    end = 150

    for i in range(start, end+1):
        if i > 1:

            for j in range(2,i):
                if i % j == 0:
                    break

            else:
                print(i)

#prime_numbers_for_given_range()          
# 
def remove_duplicates_from_array():

    arr = [1,1,1,2,2,3,3,4]          

    new_arr = list(set(arr))

    print(new_arr)

#remove_duplicates_from_array()                     


def remove_white_spaces():

    string_input = "c o d e"
    string_lst = list(string_input)
    new_string_lst = []

    for i in string_lst:
        if i.isalpha():
            new_string_lst.append(i)

    print(''.join(new_string_lst))         

#remove_white_spaces()    

def strings_are_anagrams():

    str1 = "listen"
    str2 = "silent"

    l1 = list(str1)
    l2 = list(str2)

    if l1.sort() == l2.sort():
        print("True")

    else:
        print("False")

#strings_are_anagrams()     

def find_vowels_in_a_string():

    str1 = "I love my India".lower()

    vowels = ""

    if "a" in str1:
        vowels = vowels + "a"
    if "e" in str1:
        vowels = vowels + "e"
    if "i" in str1:
        vowels = vowels + "i"
    if "o" in str1:
        vowels = vowels + "o"
    if "u" in str1:
        vowels = vowels + "u"                

    print("Vowles : ", vowels)

#find_vowels_in_a_string()           

def prime_numbers_for_range():

    start = 100
    end = 200

    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break

            else:
                print(num)        

prime_numbers_for_range()