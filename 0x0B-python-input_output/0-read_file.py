#!/usr/bin/python3

"""Module defines read_file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Parameter:
    filename (str): file to read from.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data)
