from typing import Type
import unittest
import math
from geometry_shape import GeometryShape
from circle import Circle
from rectangle import Rectangle
from cube import Cube
from sphere import Sphere

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
    
    # Cube with x = 1, y = 1, z = 1 and side = 4
    def create_cube(self) -> Cube:
        return Cube(1, 1, 1, 4)
    
    # Sphere with x = 1, y = 1, z = 1 and radius 5
    def create_sphere(self) -> Sphere:
        return Sphere(1, 1, 1, 5)
    
    # GeometryShape class test
    def test_create_geometry_shape(self):
        shape = self.create_geometry_shape()
        self.assertEqual((shape.x, shape.y), (self.x, self.y))
    
    def test_geometry_shape_invalid_x_type(self):
        with self.assertRaises(TypeError):
            shape = GeometryShape("1", 1)
    
    def test_geometry_shape_invalid_y_type(self):
        with self.assertRaises(TypeError):
            shape = GeometryShape(1, "1")

    def test_translate(self):
        shape1 = self.create_geometry_shape()
        shape2 = GeometryShape(5, 5)
        shape1.translate(5, 5)
        self.assertEqual((shape1.x, shape1.y), (shape2.x, shape2.y))
        
    def test_translate_invalid_x_type(self):
        shape = self.create_geometry_shape()
        with self.assertRaises(TypeError):
            shape.translate("5", 5)
            
    def test_translate_invalid_y_type(self):
        shape = self.create_geometry_shape()
        with self.assertRaises(TypeError):
            shape.translate(5, "5")
    
    # Circle class tests
    def test_create_circle(self):
        circle1 = self.create_circle()
        circle2 = Circle(1, 1, 5)
        self.assertEqual(circle1.radius, circle2.radius)
    
    def test_circle_invalid_radius_type(self):
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
    
    def test_rectangle_invalid_side_horizontal_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, 1, "8", 4)
    
    def test_rectangle_invalid_side_vertical_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, 1, 8, "4")
    
    def test_rectangle_area(self):
        self.assertEqual(self.create_rectangle().area(), 8 * 4)
        
    def test_rectangle_circumference(self):
        self.assertEqual(self.create_rectangle().circumference(), 2 * (8 + 4))
    
    def test_rectangle_equal(self):
        self.assertTrue(self.create_rectangle() == Rectangle(2, 2, 8, 4))
    
    def test_rectangle_equal_fale(self):
        self.assertFalse(self.create_rectangle() == Rectangle(2, 2, 7, 3))
    
    def test_rectangle_equal_invalid_type(self):
        self.assertFalse(self.create_rectangle() == GeometryShape(1, 1))
        
    def test_rectangle_is_inside(self):
        for x in range(-3, 5):
            for y in range(-1, 3):
                self.assertTrue(self.create_rectangle().is_inside(x, y))
                
    def test_rectangle_is_inside_false_x(self):
        self.assertFalse(self.create_rectangle().is_inside(10, 1))
    
    def test_rectangle_is_inside_false_y(self):
        self.assertFalse(self.create_rectangle().is_inside(1, 10))
    
    def test_rectangle_is_inside_invalid_type_x(self):
        with self.assertRaises(TypeError):
            self.create_circle().is_inside("1", 1)
    
    def test_rectangle_is_inside_invalid_type_y(self):
        with self.assertRaises(TypeError):
            self.create_circle().is_inside(1, "1")
            
    # Cube class tests
    def test_create_cube(self):
        cube1 = self.create_cube()
        cube2 = Cube(2, 2, 2, 4)
        self.assertEqual(cube1.side, cube2.side)
        
    def test_cube_invalid_side_type(self):
        with self.assertRaises(TypeError):
            cube = Cube(1, 1, 1, "4")
            
    def test_cube_translate(self):
        cube = self.create_cube()
        cube2 = Cube(5, 5, 5, 4)
        cube.translate(5, 5, 5)
        self.assertEqual((cube.x, cube.y, cube.z), (cube2.x, cube2.y, cube2.z))
            
    def test_cube_area(self):
        self.assertEqual(self.create_cube().area(), 6 * (4 ** 2))
        
    def test_cube_perimeter(self):
        self.assertEqual(self.create_cube().perimeter(), 12 * 4)
        
    def test_cube_equal(self):
        self.assertTrue(self.create_cube() == Cube(2, 2, 2, 4))
    
    def test_cube_equal_false(self):
        self.assertFalse(self.create_cube() == Cube(2, 2, 2, 5))
        
    def test_cube_equal_invalid_type(self):
        self.assertFalse(self.create_cube() == GeometryShape(1, 1))
    
    def test_cube_is_inside(self):
        for x in range(-1, 3):
            for y in range(-1, 3):
                for z in range(-1, 3):
                    self.assertTrue(self.create_cube().is_inside(x, y, z))
    
    def test_cube_is_inside_false_x(self):
        self.assertFalse(self.create_cube().is_inside(10, 1, 1))
        
    def test_cube_is_inside_false_y(self):
        self.assertFalse(self.create_cube().is_inside(1, 10, 1))
    
    def test_cube_is_inside_false_z(self):
        self.assertFalse(self.create_cube().is_inside(1, 1, 10))
        
    def test_cube_is_inside_invalid_x_type(self):
        with self.assertRaises(TypeError):
            cube = self.create_cube().is_inside("1", 1, 1)
    
    def test_cube_is_inside_invalid_y_type(self):
        with self.assertRaises(TypeError):
            cube = self.create_cube().is_inside(1, "1", 1)
            
    def test_cube_is_inside_invalid_z_type(self):
        with self.assertRaises(TypeError):
            cube = self.create_cube().is_inside(1, 1, "1")
            
    # Sphere class tests
    
    def test_create_sphere(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(1, 1, 1, 5)
        self.assertEqual(sphere1.radius, sphere2.radius)
        
    def test_sphere_invalid_radius_type(self):
        with self.assertRaises(TypeError):
            sphere = Sphere(1, 1, 1, "5")
            
    def test_sphere_translate(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(5, 5, 5, 5)
        sphere1.translate(5, 5, 5)
        self.assertEqual((sphere1.x, sphere1.y, sphere1.z), (sphere2.x, sphere2.y, sphere2.z))

    def test_sphere_translate_invalid_z_type(self):
        with self.assertRaises(TypeError):
            sphere = Sphere(1, 1, "1", 5)

    def test_sphere_circumference(self):
        self.assertEqual(self.create_sphere().circumference(), 2 * math.pi * 5)
        
    def test_sphere_is_inside(self):
        self.assertTrue(self.create_sphere().is_inside(2, 2, 2))
        
    def test_sphere_is_inside_x_false(self):
        self.assertFalse(self.create_sphere().is_inside(10, 2, 2))
    
    def test_sphere_is_inside_y_false(self):
        self.assertFalse(self.create_sphere().is_inside(2, 10, 2))
        
    def test_sphere_is_inside_z_false(self):
        self.assertFalse(self.create_sphere().is_inside(2, 2, 10))

    def test_sphere_equal(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(2, 2, 2, 5)
        self.assertTrue(sphere1 == sphere2)
        
    def test_sphere_equal_false(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(2, 2, 2, 10)
        self.assertFalse(sphere1 == sphere2)
        
    def test_sphere_equal_invalid_type(self):
        sphere1 = self.create_sphere()
        sphere2 = GeometryShape(1, 1)
        self.assertFalse(sphere1 == sphere2)

if __name__ == "__main__":
    unittest.main()