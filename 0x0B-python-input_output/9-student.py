#!/usr/bin/python3
"""Module defines student class"""


class Student:
    """Defines student class

    Attribute:
        first_name:
        last_name:
        age:

    Method:
        __init__: instatiation of attributes.
        to_json: retrieves a dictionary.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
