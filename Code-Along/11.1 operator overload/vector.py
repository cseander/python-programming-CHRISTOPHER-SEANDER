from typing import Tuple, Type


class Vector:
    def __init__(self, *numbers: float) -> None:
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} must be a float or int, not {type(number)}")
            
        if len(numbers) <= 0:
            raise ValueError("Vectors cant be empty")
        
        self._numbers = tuple(float(number) for number in numbers)
        
    @property
    def numbers(self) -> tuple:
        return self._numbers
    
    def __add__(self, other: "Vector") -> "Vector":
        if self.validate_vectors(other):
            numbers = (a+b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)
    
    def __len__(self) -> int:
        """ returns number of components in Vector """
        return len(self.numbers)
    
    def validate_vectors(self, other: "Vector") -> bool:
        """ validates that the vectors has the same dimensions """
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError("Both must be Vector and same length")
        return len(self) == len(other)
    
    def __repr__(self) -> str:
        return f"Vector:{self.numbers}"
    
    def __str__(self) -> str:
        return f"{self.numbers}"
    
    def __getitem__(self, item: int) -> float:
        return self.numbers[item]