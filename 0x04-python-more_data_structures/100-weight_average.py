#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    ab = 0
    c = 0
    for i in my_list:
        ab += (i[0] * i[1])
        c += i[1]
    return ab / c
