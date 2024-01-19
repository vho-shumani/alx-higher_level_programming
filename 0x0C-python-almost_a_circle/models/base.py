#!/usr/bin/python3
"""Module defines Base class"""
import json
import csv


class Base:
    """Base class for other model classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor to initialize Base objects

        Args:
            id(int, optional): id for object, has default value of None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is not None:
            json_string = json.dumps(list_dictionaries)
            return json_string
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """converts a json string to a list"""
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances
        """
        if list_objs is None:
            dic_list = []
        else:
            dic_list = [i.to_dictionary() for i in list_objs]
        json_str = cls.to_json_string(dic_list)
        if 'Rectangle' in f'{cls}':
            with open("Rectangle.json", "w") as f:
                f.write(json_str)
        elif 'Square' in f'{cls}':
            with open("Square.json", "w") as f:
                f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Returns a instance with all attributes set

        Args:
            dictionary: attributes to initialize
        """
        if dictionary is not None and dictionary != {}:
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances

        Return:
            empty list: if the file doesnt exist
            list of instantiated classes
        """
        try:
            if 'Rectangle' in f'{cls}':
                with open("Rectangle.json", "r") as f:
                    dic_list = Base.from_json_string(f.read())
                    return [cls.create(**i) for i in dic_list]
            elif 'Square' in f'{cls}':
                with open("Square.json", "r") as f:
                    dic_list = Base.from_json_string(f.read())
                    return [cls.create(**i) for i in dic_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CVs

        list_objs: list of instances
        """
        if 'Rectangle' in f'{cls}':
            with open("Rectangle.json", "w") as f:
                if list_objs is None or len(list_objs) == 0:
                    f.write("[]")
                format = ["id", "width", "height", "x", "y"]
                msg = csv.DictWriter(f, fieldnames=format)
                for obj in list_objs:
                    msg.writerow(obj.to_dictionary())
        elif 'Square' in f'{cls}':
            with open("Square.json", "w") as f:
                if list_objs is None or len(list_objs) == 0:
                    f.write("[]")
                format = ["id", "size", "x", "y"]
                msg = csv.DictWriter(f, fieldnames=format)
                for obj in list_objs:
                    msg.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Return:
            empty list: if the file doesnt exist
            list of instantiated classes
        """
        try:
            if 'Rectangle' in f'{cls}':
                with open("Rectangle.json", "r") as f:
                    format = ["id", "width", "height", "x", "y"]
                    dic_list = csv.DictReader(f, fieldnames=format)
                    dic_list = [dict([key, int(val)] for key, val in i.items())
                                for i in dic_list]
                    return [cls.create(**i) for i in dic_list]
            elif 'Square' in f'{cls}':
                with open("Square.json", "r") as f:
                    format = ["id", "size", "x", "y"]
                    dic_list = csv.DictReader(f, fieldnames=format)
                    dic_list = [dict([key, int(val)] for key, val in i.items())
                                for i in dic_list]
                    return [cls.create(**i) for i in dic_list]
        except FileNotFoundError:
            return []
