from geometry_shape import GeometryShape
import math

class Circle(GeometryShape):
    """A class to represent a circle"""
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y)
        self.radius = radius
        
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"radius has to be a float or int, not {type(value)}")
        self._radius = value

    def area(self) -> float:
        """Returns the area of the circle"""
        return math.pi * (self.radius ** 2)
    
    def circumference(self) -> float:
        """Returns the circumference of the circle"""
        return 2 * math.pi * self.radius
    
    def __eq__(self, other: "Circle") -> bool:
        """Validates if both are circles and have the same radius"""
        if not type(self) == type(other):
            return False
        return self.radius == other.radius
    
    # found this https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
    # for how to check multiple variables in one "isinstance"
    def is_inside(self, x: float, y: float) -> bool:
        """Validates if point is inside the circle"""
        if not all(isinstance(value, (float, int)) for value in (x, y)):
            raise TypeError("x and y has to be float or int")
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2) <= self.radius

    def __repr__(self) -> str:
        """Returns the area, circumference and center point"""
        return f"circle with area: {round(self.area(), 2)}, circumference: {round(self.circumference(), 2)} and center point in {self.x, self.y}"