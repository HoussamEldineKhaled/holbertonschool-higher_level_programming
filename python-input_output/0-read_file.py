#!/usr/bin/python3
"""just reading"""

def read_file(filename=""):
    """read text file

    Args:
       filename (str): name of file
    """
    with open(filename, encoding="UTF-8") as file:
        print(f.read(), end="")
