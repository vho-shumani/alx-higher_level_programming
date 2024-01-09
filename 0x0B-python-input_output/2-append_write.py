#!/usr/bin/python3

"""Module defines append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)

    Args:
        filename: file to append string in.
        text: string to append.

    Retrun:
        the number of characters appended.
    """
    with open(filename, 'a') as f:
        return f.write(text)
