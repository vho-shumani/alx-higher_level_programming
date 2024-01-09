#!/usr/bin/python3
import json

"""Module defines to_json_string function"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj: object

    return:
        JSON representation of an object (string)
    """
    json_string = json.dumps(my_obj)
    return json_string
