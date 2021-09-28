from typing import Type

class GeometryShape:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"x has to be a float or int, not {type(value)}")
        self._x = value
    
    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"y has to be a float or int, not {type(value)}")
        self._y = value
        
    def translate(self, new_x: float, new_y: float) -> None:
        self.x = new_x
        self.y = new_y