from figure import Figure


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        super().__init__('Triangle')
        self.a = a
        self.b = b
        self.c = c
        self.check_if_can_create_triangle(a, b, c)

    @property
    def area(self) -> float:
        half_meter = self.perimeter / 2
        area = (half_meter * (half_meter - self.a) * (half_meter - self.b) * (half_meter - self.b)) ** 0.5
        return round(area, 2)

    @property
    def perimeter(self) -> float:
        return self.a + self.b + self.c

    @staticmethod
    def check_if_can_create_triangle(a: float, b: float, c: float):
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {a}, {b}, {c}')

        if not (a + b > c and a + c > b and c + b > a):
            raise ValueError(f'Unable to create a triangle with sides: {a}, {b}, {c}')


b = Triangle(5, 2, 6)
print(b.area)
print(b.perimeter)
