#!/usr/bin/python3
"""Module define TestRectangle class"""
import unittest
from models.rectangle import Rectangle
import io
import sys

class TestRectangle(unittest.TestCase):
    """Test cases for testing rectangle methods"""
    def test_init(self):
        """Test initialization with valid and invalid values."""
        rect = Rectangle(5, 4)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

        
        with self.assertRaises(TypeError):
            Rectangle("invalid", 4)  
        with self.assertRaises(ValueError):
            Rectangle(-5, 4)  

    def test_init_optional_args(self):
        """test the contravtor"""
        rect = Rectangle(5, 4, 2, 1)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)
  
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 4, "invalid", 1) 
 
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 4, 2, "invalid")
            
    def test_width(self):
        """Test width getter and setter."""
        rect = Rectangle(5, 4)
        rect.width = 10
        self.assertEqual(rect.width, 10)

        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height(self):
        """Test height getter and setter."""
        rect = Rectangle(5, 4)
        rect.height = 8
        self.assertEqual(rect.height, 8)
        
        with self.assertRaises(ValueError):
            rect.height = -2
        
        with self.assertRaises(TypeError):
            rect.height = '10'

    def test_x(self):
        """test x getter and setter."""
        rect = Rectangle(5, 4, 2 )
        self.assertEqual(rect.x, 2)
        
        with self.assertRaises(ValueError):
            rect.x = -1
        
        with self.assertRaises(TypeError):
            rect.x = '10'
            
    def test_y(self):
        """test y getter and setter"""
        rect = Rectangle(5, 4, 2, 3)
        rect.y = 1
        self.assertEqual(rect.y, 1)
        
        with self.assertRaises(ValueError):
            rect.y = -1
            
        with self.assertRaises(TypeError):
            rect.y = '10'
            
    def test_area(self):
        "test area() method"
        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)
        
        rect1 = Rectangle(2, 3)
        rect1.height = 10
        self.assertEqual(rect1.area(), 20)
        
    def test_display(self):
        """Test the display method's output."""
        rect = Rectangle(2, 3)  
        captured_output = io.StringIO()  
        sys.stdout = captured_output  

        rect.display()  

        sys.stdout = sys.__stdout__  
        expected_output = "##\n##\n##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        
        rect = Rectangle(2, 3, 2, 2)  
        captured_output = io.StringIO()  
        sys.stdout = captured_output  

        rect.display()  

        sys.stdout = sys.__stdout__  
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        
    def test_update_method(self):
        """test the update method"""
        rect = Rectangle(5, 4)

        rect.update(height=8)
        self.assertEqual(rect.height, 8)

        rect.update(width=2, x=1, y=2)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_to_dictionary(self):
        """test to_dictionary method"""
        rect = Rectangle(5, 4, 2, 1)
        expected_dict = {
            "id": rect.id,
            "width": 5,
            "height": 4,
            "x": 2,
            "y": 1,
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_str(self):
        """tests the str method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1, 'Rectangle] (12) 2/1 - 4/6')
            