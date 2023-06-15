#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            keys.append(i)
    for i in keys:
        a_dictionary.pop(i)
    return a_dictionar
