#!/usr/bin/python3
"""print a sorted list"""


class MyList(list):
    """
    print a sorted list
    """

    def print_sorted(self):
        print("{}".format(sorted(self)))
