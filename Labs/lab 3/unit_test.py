import unittest
from geometry_shape import GeometryShape

class TestGeometryShape(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 1
        
    def create_geometry_shape(self) -> GeometryShape:
        return GeometryShape(self.x, self.y)
        
    def test_create_geometry_shape(self) -> None:
        shape = self.create_geometry_shape()
        self.assertEqual(shape.x, self.x)
        self.assertEqual(shape.y, self.y)
    
    def test_create_invalid_xy(self) -> None:
        with self.assertRaises(TypeError):
            shape = GeometryShape("1", 1)
            shape = GeometryShape(1, "1")

    def test_translate(self) -> None:
        shape = self.create_geometry_shape()
        shape.translate(5, 5)
        
    def test_translate_invalid_xy(self) -> None:
        shape = self.create_geometry_shape()
        with self.assertRaises(TypeError):
            shape.translate("5", 5)
            shape.translate(5, "5")
        
if __name__ == "__main__":
    unittest.main()