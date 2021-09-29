from math import ceil
from geometry_shape import GeometryShape

class Cube(GeometryShape):
    def __init__(self, x: float, y: float, z: float, side: float) -> None:
        super().__init__(x, y)
        self.z = z
        self.side = side
    
    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"z has to be a float or int, not {type(value)}")
        self._z = value
        
    @property
    def side(self) -> float:
        return self._side
    
    @side.setter
    def side(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"side has to be a float or int, not {type(value)}")
        self._side = value
        
    def translate(self, new_x: float, new_y: float, new_z: float) -> None:
        """Moves the cube to new coordinates"""
        super().translate(new_x, new_y)
        self.z = new_z

    def area(self) -> float:
        """Returns the surface area of the cube"""
        return 6 * (self.side ** 2)
    
    # Note: a cube does not have a circumference it has a perimeter
    def perimeter(self) -> float:
        """Returns the perimeter of the cube"""
        return 12 * self.side
    
    def __eq__(self, other: "Cube") -> bool:
        """Validates that both are cube and have the same sides"""
        if not type(self) == type(other):
            return False
        return self.side == other.side
    
    def is_inside(self, x: float, y: float, z: float):
        """Validates if point is inside the cube"""
        if not all(isinstance(value, (float, int)) for value in (x, y, z)):
            raise TypeError("x, y and z has to be float or int")
        xyz_inside = ((self.x - (self.side / 2)) <= x <= (self.x + (self.side / 2)),
                      (self.y - (self.side / 2)) <= y <= (self.y + (self.side / 2)),
                      (self.z - (self.side / 2)) <= z <= (self.z + (self.side / 2)))
        return all(xyz_inside)
    
    def __repr__(self) -> str:
        """Returns the area, perimeter and coordinates of the cube"""
        return f"cube with area: {self.area()}, perimeter: {self.perimeter()} and center in {self.x, self.y, self.z}"
    