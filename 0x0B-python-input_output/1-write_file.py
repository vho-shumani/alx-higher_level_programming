#!/usr/bin/python3

"""Module defines write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename: file to write in.
        text: text to write.

    Return:
        the number of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
