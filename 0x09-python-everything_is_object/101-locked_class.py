#!/usr/bin/python3

"""defines a locked class"""


class LockedClass:
    """prevent creation of new instance attribute,
    except instance attribute first_name"""
    __slots__ = ["first_name"]
