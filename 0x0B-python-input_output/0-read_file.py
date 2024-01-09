#!/usr/bin/python3

"""Module defines read_file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Parameter:
    filename: file to read from.
    """
    with open(filename, 'r') as f:
        print(f.read())
