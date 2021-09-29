import unittest
import math
from geometry_shape import GeometryShape
from circle import Circle

class TestGeometryShape(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 1
    
    # GeometryShape with x = 1 and y = 1
    def create_geometry_shape(self) -> GeometryShape:
        return GeometryShape(self.x, self.y)
    
    # Circle with x = 1, y = 1 and radius = 5
    def create_circle(self) -> Circle:
        return Circle(self.x, self.y, 5)
    
    def test_create_geometry_shape(self):
        shape = self.create_geometry_shape()
        self.assertEqual((shape.x, shape.y), (self.x, self.y))
    
    def test_create_geometry_shape_invalid_xy(self):
        with self.assertRaises(TypeError):
            shape = GeometryShape("1", 1)
            shape = GeometryShape(1, "1")

    def test_translate(self):
        shape1 = self.create_geometry_shape()
        shape2 = GeometryShape(5, 5)
        shape1.translate(5, 5)
        self.assertEqual((shape1.x, shape1.y), (shape2.x, shape2.y))
        
    def test_translate_invalid_xy(self):
        shape = self.create_geometry_shape()
        with self.assertRaises(TypeError):
            shape.translate("5", 5)
            shape.translate(5, "5")
    
    def test_create_circle(self):
        circle1 = self.create_circle()
        circle2 = Circle(1, 1, 5)
        self.assertEqual(circle1.radius, circle2.radius)
    
    def test_create_circle_invalid_radius(self):
        with self.assertRaises(TypeError):
            circle = Circle(1, 1, "1")
    
    def test_circle_area(self):
        self.assertEqual(self.create_circle().area(), math.pi * (5 ** 2))
    
    def test_circle_circumference(self):
        self.assertEqual(self.create_circle().circumference(), 2 * math.pi * 5)
        
    def test_circle_equal(self):
        self.assertTrue(self.create_circle() == Circle(1, 1, 5))
        
    def test_circle_equal_false(self):
        self.assertFalse(self.create_circle() == Circle(1, 1, 10))
        
    def test_circle_equal_invalid_type(self):
        self.assertFalse(self.create_circle() == GeometryShape(1, 1))
        
    def test_circle_is_inside(self):
        self.assertTrue(self.create_circle().is_inside(2, 2))
    
    def test_circle_is_inside_false(self):
        self.assertFalse(self.create_circle().is_inside(10, 10))
        
    def test_circle_is_inside_invalid_type(self):
        with self.assertRaises(TypeError):
            self.create_circle().is_inside("2", 2)
        
if __name__ == "__main__":
    unittest.main()