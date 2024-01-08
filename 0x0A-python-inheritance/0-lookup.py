#!/usr/bin/python3

"""Module defines lookup function"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object

    arg:
    obj: object to list its attributes and methhods.

    returns:
    list: available attributes and methods of an object
    """
    return dir(obj)
