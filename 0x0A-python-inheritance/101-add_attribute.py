#!/usr/bin/python3

"""Module defines function to add attribute"""


def add_attribute(obj, var, val):
    """Adds a new attribute to an object if possible,
    raising a TypeError otherwise.

    Args:
        obj: The object to add the attribute to.
        name: The name of the new attribute.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes added.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, var, val)
    else:
        raise TypeError("can't add new attribute")
