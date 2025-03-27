#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range (0, list_length):
        try:
            quotiant = my_list_1[i] /my_list_2[i]
        except IndexError:
            print("out of range")
            quotiant = 0
        except (TypeError, ZeroDivisionError):
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                print("division by 0" if my_list_2[i] == 0 else "wrong type")
            else:
                print("wrong type")
            quotiant = 0
        finally:
            new_list.append(quotiant)
    return new_list
