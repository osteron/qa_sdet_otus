import pytest
from OOP.src.square import Square


class TestPositive:
    @pytest.mark.parametrize('side_a', [5, 2.3])
    def test_square_creation(self, side_a):
        square = Square(side_a)
        assert square.name == 'Square', 'Expected name is "Square"'

    @pytest.mark.parametrize('side_a, expected_perimeter', [(5, 20), (2.3, 9.2)])
    def test_square_perimeter_calculation(self, side_a, expected_perimeter):
        square = Square(side_a)
        assert square.perimeter == expected_perimeter, 'Expected correct perimeter'

    @pytest.mark.parametrize('side_a, expected_area', [(5, 25), (2.3, 5.29)])
    def test_square_area_calculation(self, side_a, expected_area):
        square = Square(side_a)
        assert square.area == expected_area, 'Expected correct area'

    @pytest.mark.parametrize('side_a_1, side_a_2, expected_sum', [(5, 1.5, 27.25)])
    def test_two_square_areas_sum(self, side_a_1, side_a_2, expected_sum):
        square_1 = Square(side_a_1)
        square_2 = Square(side_a_2)
        assert square_1.add_area(square_2) == expected_sum, f'Expected sum is {expected_sum}'


class TestNegative:
    @pytest.mark.parametrize('side_a', [0, -1], ids=['side is zero', 'side is negative'])
    def test_square_create_error(self, side_a):
        with pytest.raises(ValueError):
            Square(side_a)

    @pytest.mark.parametrize('some_other_class', [5, 2.5, 'something'], ids=['integer', 'float', 'str'])
    def test_two_square_areas_sum_error(self, some_other_class):
        square_1 = Square(5)
        with pytest.raises(ValueError):
            square_1.add_area(some_other_class)
