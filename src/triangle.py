from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__('Triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.check_sides_greater_than_zero(side_a, side_b, side_c)
        self.check_the_existence_of_a_triangle(side_a, side_b, side_c)

    @property
    def area(self) -> float:
        half_meter = self.perimeter / 2
        area = \
            (half_meter * (half_meter - self.side_a) * (half_meter - self.side_b) * (half_meter - self.side_c)) ** 0.5
        return round(area, 1)

    @property
    def perimeter(self) -> float:
        return round(self.side_a + self.side_b + self.side_c, 1)

    @staticmethod
    def check_sides_greater_than_zero(side_a: float, side_b: float, side_c: float):
        if not (side_a > 0 and side_b > 0 and side_c > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {side_a}, {side_b}, {side_c}')

    @staticmethod
    def check_the_existence_of_a_triangle(side_a: float, side_b: float, side_c: float):
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_c + side_b > side_a):
            raise ValueError(f'Unable to create a triangle with sides: {side_a}, {side_b}, {side_c}')
