#!/usr/bin/python3
"""write appending"""


def append_write(filename="", text=""):
    """append write method

    Args:
       filename (str): name of the file
       text (str): content of file
    """

    with open(filename, "a", encode="UTF-8") as file:
        return file.write(text)
