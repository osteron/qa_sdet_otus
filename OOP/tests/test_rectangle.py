import pytest
from OOP.src.rectangle import Rectangle


class TestPositive:
    @pytest.mark.parametrize('side_a, side_b', [(2, 5), (1.5, 3.4)])
    def test_rectangle_creation(self, side_a, side_b):
        rectangle = Rectangle(side_a, side_b)
        assert rectangle.name == "Rectangle", 'Expected name is "Rectangle"'

    @pytest.mark.parametrize('side_a, side_b, expected_perimeter', [(2, 5, 14), (1.5, 3.4, 9.8)])
    def test_rectangle_perimeter_calculation(self, side_a, side_b, expected_perimeter):
        rectangle = Rectangle(side_a, side_b)
        assert rectangle.perimeter == expected_perimeter, 'Expected correct perimeter'

    @pytest.mark.parametrize('side_a, side_b, expected_area', [(2, 5, 10), (1.5, 3.4, 5.1)])
    def test_rectangle_area_calculation(self, side_a, side_b, expected_area):
        rectangle = Rectangle(side_a, side_b)
        assert rectangle.area == expected_area, 'Expected correct area'

    @pytest.mark.parametrize('side_a_1, side_b_1, side_a_2, side_b_2, expected_sum', [(2, 4, 3, 6, 26)])
    def test_two_rectangle_areas_sum(self, side_a_1, side_b_1, side_a_2, side_b_2, expected_sum):
        rectangle_1 = Rectangle(side_a_1, side_b_1)
        rectangle_2 = Rectangle(side_a_2, side_b_2)
        assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'


class TestNegative:
    @pytest.mark.parametrize('side_a, side_b', [(0, 2), (3, -1)], ids=['side is zero', 'side is negative'])
    def test_rectangle_create_error(self, side_a, side_b):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)

    @pytest.mark.parametrize('some_other_class', [10, 2.3, 'something'], ids=['integer', 'float', 'str'])
    def test_two_rectangle_ares_sum_error(self, some_other_class):
        rectangle_1 = Rectangle(3, 4)
        with pytest.raises(ValueError):
            rectangle_1.add_area(some_other_class)
