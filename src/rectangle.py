from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        super().__init__('Rectangle')
        self.side_a = side_a
        self.side_b = side_b
        self.check_if_can_create_rectangle(side_a, side_b)

    @property
    def area(self) -> float:
        return round(self.side_a * self.side_b, 2)

    @property
    def perimeter(self) -> float:
        return round((self.side_a + self.side_b) * 2, 2)

    @staticmethod
    def check_if_can_create_rectangle(side_a: float, side_b: float):
        if not (side_a > 0 and side_b > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {side_a}, {side_b}')
