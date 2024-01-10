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

    def to_json(self, attrs=None):
        dic = {}
        if isinstance(attrs, list) and all(isinstance(elem, str) for elem in attrs):
            for i in attrs:
                if hasattr(self, i):
                    dic[i] = getattr(self, i)
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): keys and value to replace the attributes.
        """
        for key, value in json.item():
            setattr(self, key, value)
