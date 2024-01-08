#!/usr/bin/python3

"""Module defines is_same_class function """


def is_same_class(obj, a_class):
    """Determines if the object is exactly an instance of the specified class

    Args:
    obj: object to check.
    a_class: class to check if the obj is a instance of.

    Returns:
    Bool: True if the object is exactly an instance
    of the specified class; otherwise False
    """
    return type(obj) == a_class
