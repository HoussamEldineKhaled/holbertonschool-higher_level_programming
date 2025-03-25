#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = set()
    sum = 0
    for i in range(0, len(my_list)):
        result.add(my_list[i])
    for i in result:
        sum += i
    return sum
