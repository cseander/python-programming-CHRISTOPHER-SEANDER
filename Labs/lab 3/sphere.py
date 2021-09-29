from geometry_shape import GeometryShape
import math

class Sphere(GeometryShape):
    def __init__(self, x: float, y: float, z: float, radius: float) -> None:
        super().__init__(x, y)
        self.z = z
        self.radius = radius
    
    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"z has to be a float or int, not {type(value)}")
        self._z = value
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"radius has to be a float or int, not {type(value)}")
        self._radius = value
        
    def translate(self, new_x: float, new_y: float, new_z: float) -> None:
        """Moves the sphere to new coordinates"""
        super().translate(new_x, new_y)
        self.z = new_z
    
    def area(self) -> float:
        """Returns the area of the sphere"""
        return 4 * math.pi * (self.radius ** 2)
    
    def circumference(self) -> float:
        """Returns the circumference of the sphere"""
        return 2 * math.pi * self.radius
    
    def is_inside(self, x: float, y: float, z: float) -> bool:
        """Validates if point is inside the sphere"""
        if not all(isinstance(value, (float, int)) for value in (x, y, z)):
            raise TypeError("x, y and z has to be float or int")
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2) <= self.radius
    
    def __eq__(self, other: "Sphere") -> bool:
        """Validates if both are spheres and have the same radius"""
        if not type(self) == type(other):
            return False
        return self.radius == other.radius
    
    def __repr__(self) -> str:
        return f"sphere with area: {self.area()}, circumference: {self.circumference()} and center in {self.x, self.y, self.z}"
