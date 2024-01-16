import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Tests base class"""
    def test_id_None(self):
        #test base class if parameter is not provided
        b1 = Base()
        b2 = Base()
        b3 = Base()
        
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        
    def test_id_value(self):
        #test base with a parameter provided
        b1 = Base(12)
        b2 = Base()
        
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 4)
        