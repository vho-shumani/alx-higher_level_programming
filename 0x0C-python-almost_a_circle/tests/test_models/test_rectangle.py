import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    
        def test_id(self):
        #test base class if parameter is not provided
            r1 = Rectangle(10, 2)
            r2 = Rectangle(2, 10)
            r3 = Rectangle(10, 2, 0, 0, 12)

            self.assertEqual(r1.id, 1)
            self.assertEqual(r2.id, 2)
            self.assertEqual(r3.id, 12)
            
        def test_getters(self):
        #test Rectangle class with parameters
            r = Rectangle(10, 12, 3 , 4)
            
            self.assertEqual(r.width, 10)
            self.assertEqual(r.height, 12)
            self.assertEqual(r.x, 3)
            self.assertEqual(r.y, 4)
    
        def test_datatype(self):
        #tests if value is a integer
            self.assertRaises(TypeError, Rectangle.width, "2")
            self.assertRaises(TypeError, Rectangle.height, {})
            self.assertRaises(TypeError, Rectangle.x, [])
            self.assertRaises(TypeError, Rectangle.y, 5j)
            
        def test_exception(self):
        #check the value of input
            self.assertRaises(ValueError, Rectangle.width, 0)
            self.assertRaises(ValueError, Rectangle.height, -1)
            self.assertRaises(ValueError, Rectangle.x, -1)
            with self.assertRaises(ValueError):
                r = Rectangle(10, 2)
                r.width = -10
                
        def test_area(self):
        #test the area of rectangle
            r = Rectangle(3, 2)
            r2 = Rectangle(2, 10)
            r3 = Rectangle(8, 7, 0, 0, 12)
            
            self.assertEqual(r.area(), 6)
            self.assertEqual(r2.area(), 20)
            self.assertEqual(r3.area(), 56)
            
        def test_display(self):
        # test the sisplay function
            r1 = Rectangle(2,4)
            r2 = Rectangle(2, 2)
            r3 = Rectangle(2, 3, 2, 2)
            r4 = Rectangle(3, 2, 1, 0)
            
            self.assertEqual(r1.display(), '##\n##\n##\n##\n')
            self.assertEqual(r2.display(), '##\n##\n')
            
            self.assertEqual(r3.display(), '\n\n  ##\n  ##\n  ##\n')

        def test_str(self):
        #test the str function
            r1 = Rectangle(4, 6, 2, 1, 12)
            r2 = Rectangle(5, 5, 1)
            
            self.assertEqual(r1, "[Rectangle] (12) 2/1 - 4/6")
            self.assertEqual(r2, "[Rectangle] (1) 1/0 - 5/5")

        def update(self, *args):
        #test the update function
            r1 = Rectangle(10, 10, 10, 10)
            r2 = Rectangle(10, 10, 10, 10)
            
            self.assertEqual(r1, "[Rectangle] (1) 10/10 - 10/10")
            self.assertEqual(r1.update(86), "[Rectangle] (89) 10/10 - 10/10")
            self.assertEqual(r1.update(89, 2), "[Rectangle] (89) 10/10 - 2/10")
            self.assertEqual(r1.update(89, 2, 3), "[Rectangle] (89) 10/10 - 2/3")
            self.assertEqual(r1.update(89, 2, 3, 4), "[Rectangle] (89) 4/10 - 2/3")
            self.assertEqual(r1.update(89, 2, 3, 4, 5), "[Rectangle] (89) 4/5 - 2/3")
            self.assertEqual(r2.update(height=1), "[Rectangle] (1) 10/10 - 10/1")
            self.assertEqual(r2.update(width=1, x=2), "[Rectangle] (1) 2/10 - 1/1")
            self.assertEqual(r2.update(y=1, width=2, x=3, id=89), "[Rectangle] (89) 3/1 - 2/1")
            self.assertEqual(r1.update(x=1, height=2, y=3, width=4), "[Rectangle] (89) 1/3 - 4/2")
