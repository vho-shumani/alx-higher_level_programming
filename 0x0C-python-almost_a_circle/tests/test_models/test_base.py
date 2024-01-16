#!/usr/bin/python3
"""Module defines TestBase class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """test cases for base methods"""
    
    def test_constructor_with_id(self):
        """Test constructor with an explicit ID."""
        b = Base(id=42)
        self.assertEqual(b.id, 42)

    def test_constructor_without_id(self):
        """Test constructor with auto-assigned ID."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string(self):
        """Test JSON string conversion."""
        data = [{'id': 1, 'name': 'Object 1'}, {'id': 2, 'name': 'Object 2'}]
        json_string = Base.to_json_string(data)
        expected_json = '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]'
        self.assertEqual(json_string, expected_json)

    def test_from_json_string(self):
        """Test JSON string parsing."""
        json_string = '[{"id": 3, "value": "Test"}]'
        parsed_data = Base.from_json_string(json_string)
        self.assertEqual(parsed_data, [{'id': 3, 'value': 'Test'}])

    def test_save_to_file(self):
        """Test saving objects to file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            output = file.read()
        self.assertEqual(output,'[{"width": 10, "height": 7, "x": 2, "y":[61 chars] 4}]')

    def test_load_from_file(self):
        """Test loading objects from file."""
        Base.save_to_file([Base(30)])  
        loaded_objects = Base.load_from_file()
        self.assertEqual([obj.id for obj in loaded_objects], [30])
