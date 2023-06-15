#!/usr/bin/python3
def no_c(my_string):
    s = f""
    for i in my_string:
        if i != 'c' and i != 'C':
            s += f"{i}"
    return s
