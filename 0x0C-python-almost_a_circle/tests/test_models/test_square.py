#!/usr/bin/python3
"""module provides test case for square class"""


import io
import sys
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """defines tests module for square class"""
    
    def test_init(self):
        """Test initialization with valid and invalid values."""
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        with self.assertRaises(TypeError):
            Square("invalid", 4)  
        with self.assertRaises(ValueError):
            Square(-5)  

    def test_size(self):
        """Test size getter and setter."""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

        with self.assertRaises(ValueError):
            square.size = 0

    def test_x(self):
        """Test x getter and setter."""
        square = Square(5, 4, 2)
        self.assertEqual(square.x, 4)
        square.x = 10
        self.assertEqual(square.x, 10)

    def test_y(self):
        """Test y getter and setter."""
        square = Square(5, 4, 2)
        self.assertEqual(square.y, 2)
        square.y = 8
        self.assertEqual(square.y, 8)

    def test_area(self):
        """Test area calculation."""
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        """Test the visual representation."""
        captured_output = io.StringIO()  
        sys.stdout = captured_output

        square = Square(4)
        square.display()

        sys.stdout = sys.__stdout__  
        expected_output = "####\n####\n####\n####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """Test string representation."""
        square = Square(5, 2, 3, 10)
        self.assertEqual(str(square), "[Square] (10) 2/3 - 5")

    def test_update(self):
        """Test updating attributes."""
        square = Square(5, 2, 3, 10)
        square.update(size=8, y=7)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.y, 7)

        square.update(id=25, x=4)  
        self.assertEqual(square.id, 25)
        self.assertEqual(square.x, 4)

    def test_to_dictionary(self):
        """Test dictionary representation."""
        square = Square(5, 2, 3, 10)
        dictionary = square.to_dictionary()
        self.assertEqual(dictionary, {'id': 10, 'size': 5, 'x': 2, 'y': 3})
