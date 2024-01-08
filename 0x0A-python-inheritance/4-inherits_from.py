#!/usr/bin/python3

"""Module defines inherits_from function"""


def inherits_from(obj, a_class):
    """determine if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
    obj: object to check in the class.
    a_class: class to check if the obj is a instance of.

    Returns:
    Bool: True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False
    """
    return issubclass(type(obj), a_class)
