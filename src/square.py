from figure import Figure


class Square(Figure):
    def __init__(self, a: float):
        super().__init__('Square')
        self.a = a
        self.check_if_can_create_square(a)

    @property
    def area(self) -> float:
        return round(self.a ** 2, 2)

    @property
    def perimeter(self) -> float:
        return round(self.a * 4, 2)

    @staticmethod
    def check_if_can_create_square(a: float):
        if a <= 0:
            raise ValueError(f'Side must be greater than 0. Got: {a}')
