from src.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius: float):
        super().__init__('Circle')
        self.radius = radius
        self.check_radius_greater_than_zero(radius)

    @property
    def area(self) -> float:
        return round(pi * self.radius ** 2, 2)

    @property
    def perimeter(self) -> float:
        return round(2 * pi * self.radius, 2)

    @staticmethod
    def check_radius_greater_than_zero(radius):
        if radius <= 0:
            raise ValueError(f'Radius must be greater than 0. Got: {radius}')

