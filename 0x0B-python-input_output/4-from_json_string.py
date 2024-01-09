#!/usr/bin/python3
"""Module defines to_json_string function"""

import json


def from_json_string(my_obj):
    """returns the object (string) of an JSON representation

    Args:
        my_obj: object

    return:
        JSON representation of an object (string)
    """
    data = json.loads(my_obj)
    return data
