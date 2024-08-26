from os import remove
import re
from turtle import st

def check_special_character(str):
    regx = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    search_special = regx.search(st)

    if search_special == None:
        print("Not found")
        
    else:
        print("Found") 
        new_Str = re.sub(regx, '', st)
        print(new_Str)

st = "hello$ambikapur" 

check_special_character(st)
