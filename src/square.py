from figure import Figure


class Square(Figure):
    def __init__(self, side_a: float):
        super().__init__('Square')
        self.side_a = side_a
        self.check_if_can_create_square(side_a)

    @property
    def area(self) -> float:
        return round(self.side_a ** 2, 2)

    @property
    def perimeter(self) -> float:
        return round(self.side_a * 4, 2)

    @staticmethod
    def check_if_can_create_square(side_a: float):
        if side_a <= 0:
            raise ValueError(f'Side must be greater than 0. Got: {side_a}')
