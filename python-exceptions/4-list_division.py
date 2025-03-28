#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range (list_length):
        try:
            quotiant = my_list_1[i] /my_list_2[i]
        except IndexError:
            print("out of range")
            quotiant = 0
        except TypeError:
            print("wrong type")
            quotiant = 0
        except ZeroDivisionError:
            print("division by 0")
            quotiant = 0
        finally:
            new_list.append(quotiant)
    return new_list
