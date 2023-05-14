from figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        super().__init__('Rectangle')
        self.a = a
        self.b = b
        self.check_if_can_create_rectangle(a, b)

    @property
    def area(self) -> float:
        return round(self.a * self.b, 2)

    @property
    def perimeter(self) -> float:
        return round((self.a + self.b) * 2, 2)

    @staticmethod
    def check_if_can_create_rectangle(a: float, b: float):
        if not (a > 0 and b > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {a}, {b}')
