#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    quotiant = 0
    for i in range (0, list_length):
        try:
            quotiant = my_list_1[i] /my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            quotiant = 0
        except IndexError:
            print("out of range")
            quotiant = 0
        except ZeroDivisionError:
            print("division by 0")
            quotiant = 0
        finally:
            new_list.append(quotiant)
    return new_list
