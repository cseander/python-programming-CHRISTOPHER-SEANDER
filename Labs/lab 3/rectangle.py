from typing import Type
from geometry_shape import GeometryShape

class Rectangle(GeometryShape):
    def __init__(self, x: float, y: float, side_horizontal: float, side_vertical: float) -> None:
        super().__init__(x, y)
        self.side_horizontal = side_horizontal
        self.side_vertical = side_vertical
        
    @property
    def side_horizontal(self) -> float:
        return self._side_horizontal
    
    @side_horizontal.setter
    def side_horizontal(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"side_horizontal has to be float or int, not {type(value)}")
        self._side_horizontal = value
        
    @property
    def side_vertical(self) -> float:
        return self._side_vertical
    
    @side_vertical.setter
    def side_vertical(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"side_vertical has to be float or int, not {type(value)}")
        self._side_vertical = value
        
    def area(self) -> float:
        """Returns the area of the rectangle"""
        return self.side_horizontal * self.side_vertical
    
    def circumference(self) -> float:
        """Returns the circumference of the rectangle"""
        return (self.side_horizontal * 2) + (self.side_vertical * 2)
    
    def __eq__(self, other: "Rectangle") -> bool:
        """Validates if both are rectangles and have the same dimensions"""
        if not type(self) == type(other):
            return False
        return (self.side_horizontal, self.side_vertical) == (other.side_horizontal, other.side_vertical)

    def is_inside(self, x: float, y: float) -> bool:
        """Validates if point is inside the rectangle"""
        if not all(isinstance(value, (float, int)) for value in (x, y)):
            raise TypeError("x and y has to be float or int")
        return (self.x - (self.side_horizontal / 2)) <= x <= (self.x + (self.side_horizontal / 2)) and (self.y - (self.side_vertical / 2)) <= y <= (self.y + (self.side_vertical / 2))
        
    def __repr__(self) -> str:
        return f"rectangle with {round(self.area(), 2)} area, {round(self.circumference(), 2)} circumference and center point in {self.x, self.y}"