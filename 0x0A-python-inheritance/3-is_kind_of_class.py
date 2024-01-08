#!/usr/bin/python3

"""Module provides is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Determines if the object is an instance of the
    specified class and subclasses

    Args:
    obj: object to check.
    a_class: class to check if the obj is a instance of.

    Returns:
    Bool: True if the object is an instance
    of the specified class and subclasses; otherwise False"""

    return isinstance(obj, a_class)
