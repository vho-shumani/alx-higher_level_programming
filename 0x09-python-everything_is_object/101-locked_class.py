#!/usr/bin/python3

class LockedClass:
    """prevent creation of new instance attribute,
    except instance attribute first_name"""
    __slot__ = ["first_name"]
