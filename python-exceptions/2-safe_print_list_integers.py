#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    if not isinstance(my_list, list):
        return 0
    if not isinstance(x, int) or x < 0:
        return 0
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except TypeError:
            continue
        except ValueError:
            continue
        except IndexError:
            raise
    print()
    return count
