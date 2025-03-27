#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range (0, list_length):
        try:
            if not (isinstance(my_list_1[i], (int, float)) or not (isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
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
