def find_common_letters():

    str1 = "NAINA"
    str2 = "REENA"

    st1 = set(str1)
    st2 = set(str2)

    common = st1 & st2

    print(common)


find_common_letters()