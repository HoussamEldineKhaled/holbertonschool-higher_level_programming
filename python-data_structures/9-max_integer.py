#!/usr/bin/python3
def max_integer(my_list=[]):
    max = -10000000
    if len(my_list) == 0:
        return "None"
    for i in range(0, len(my_list)):
        if max < my_list[i]:
            max = my_list[i]

    return max
