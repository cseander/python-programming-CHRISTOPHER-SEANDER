from typing import Type
import unittest
import math
from geometry_shape import GeometryShape
from circle import Circle
from rectangle import Rectangle

class TestGeometryShape(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 1
    
    # GeometryShape with x = 1 and y = 1
    def create_geometry_shape(self) -> GeometryShape:
        return GeometryShape(self.x, self.y)
    
    # Circle with x = 1, y = 1 and radius = 5
    def create_circle(self) -> Circle:
        return Circle(self.x, self.y, 5)
    
    # Rectangle with x = 1, y = 1, side_horizontal = 8 and side_vertical = 4
    def create_rectangle(self) -> Rectangle:
        return Rectangle(1, 1, 8, 4)
    
    # GeometryShape class test
    def test_create_geometry_shape(self):
        shape = self.create_geometry_shape()
        self.assertEqual((shape.x, shape.y), (self.x, self.y))
    
    def test_geometry_shape_invalid_x(self):
        with self.assertRaises(TypeError):
            shape = GeometryShape("1", 1)
    
    def test_geometry_shape_invalid_y(self):
        with self.assertRaises(TypeError):
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
    
    # Circle class tests
    def test_create_circle(self):
        circle1 = self.create_circle()
        circle2 = Circle(1, 1, 5)
        self.assertEqual(circle1.radius, circle2.radius)
    
    def test_circle_invalid_radius(self):
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
            
    # Rectangle class tests
    def test_create_rectangle(self):
        rectangle1 = self.create_rectangle()
        rectangle2 = Rectangle(1, 1, 8, 4)
        self.assertEqual((rectangle1.side_horizontal, rectangle1.side_vertical), (rectangle2.side_horizontal, rectangle2.side_vertical))
    
    def test_rectangle_invalid_side_horizontal(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, 1, "8", 4)
    
    def test_rectangle_invalid_side_vertical(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, 1, 8, "4")
    
    def test_rectangle_area(self):
        self.assertEqual(self.create_rectangle().area(), 8 * 4)
        
    def test_rectangle_circumference(self):
        self.assertEqual(self.create_rectangle().circumference(), (8 * 2) + (4 * 2))
    
    def test_rectangle_equal(self):
        self.assertTrue(self.create_rectangle() == Rectangle(2, 2, 8, 4))
    
    def test_rectangle_equal_fale(self):
        self.assertFalse(self.create_rectangle() == Rectangle(2, 2, 7, 3))
    
    def test_rectangle_equal_invalid_type(self):
        self.assertFalse(self.create_rectangle() == GeometryShape(1, 1))

if __name__ == "__main__":
    unittest.main()